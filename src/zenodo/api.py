"""Zenodo API client — all HTTP calls go through here."""

import json
import ssl
import time
import urllib.request
import urllib.error
from pathlib import Path


class ZenodoAPIError(Exception):
    """Raised when a Zenodo API call fails."""
    def __init__(self, status_code: int, message: str, deposition_id: int = None):
        self.status_code = status_code
        self.deposition_id = deposition_id
        super().__init__(f"Zenodo API {status_code}: {message}")


# Shared SSL context — use system defaults (verifies certificates)
_ctx = ssl.create_default_context()


class ZenodoClient:
    """Low-level Zenodo API client."""

    def __init__(self, token: str, sandbox: bool = True):
        self.token = token
        self.sandbox = sandbox
        self.base_url = (
            "https://sandbox.zenodo.org/api" if sandbox
            else "https://zenodo.org/api"
        )

    def _request(self, method: str, path: str, data=None, headers=None,
                 timeout: int = 60, retries: int = 1) -> dict:
        """Make an authenticated request to the Zenodo API."""
        url = f"{self.base_url}{path}"
        hdrs = {"Authorization": f"Bearer {self.token}"}
        if headers:
            hdrs.update(headers)

        if data is not None and isinstance(data, dict):
            data = json.dumps(data).encode("utf-8")
            hdrs["Content-Type"] = "application/json"

        for attempt in range(retries + 1):
            req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
            try:
                with urllib.request.urlopen(req, timeout=timeout, context=_ctx) as resp:
                    body = resp.read().decode("utf-8")
                    return json.loads(body) if body.strip() else {}
            except urllib.error.HTTPError as e:
                error_body = e.read().decode("utf-8", errors="replace")
                if e.code >= 500 and attempt < retries:
                    time.sleep(5)
                    continue
                raise ZenodoAPIError(e.code, error_body)
            except urllib.error.URLError as e:
                if attempt < retries:
                    time.sleep(5)
                    continue
                raise ZenodoAPIError(0, str(e))

    def create_deposition(self) -> dict:
        """Create an empty deposition. Returns full deposition dict."""
        return self._request("POST", "/deposit/depositions", data={})

    def upload_file(self, deposition_id: int, filepath: Path,
                    filename: str = None) -> dict:
        """Upload a file to a deposition via the bucket API."""
        fname = filename or filepath.name
        # Get the bucket URL from the deposition
        dep = self._request("GET", f"/deposit/depositions/{deposition_id}")
        bucket_url = dep.get("links", {}).get("bucket")
        if not bucket_url:
            raise ZenodoAPIError(0, f"No bucket URL for deposition {deposition_id}")

        # Upload via PUT to bucket
        file_data = filepath.read_bytes()
        url = f"{bucket_url}/{fname}"
        req = urllib.request.Request(
            url, data=file_data, method="PUT",
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/octet-stream",
            }
        )
        try:
            with urllib.request.urlopen(req, timeout=300, context=_ctx) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            raise ZenodoAPIError(e.code, e.read().decode("utf-8", errors="replace"),
                               deposition_id)

    def set_metadata(self, deposition_id: int, metadata: dict) -> dict:
        """Set metadata on a deposition."""
        return self._request(
            "PUT", f"/deposit/depositions/{deposition_id}",
            data={"metadata": metadata}
        )

    def publish(self, deposition_id: int) -> dict:
        """Publish a deposition. Returns dict with 'doi' and links."""
        return self._request(
            "POST", f"/deposit/depositions/{deposition_id}/actions/publish"
        )

    def delete_deposition(self, deposition_id: int) -> bool:
        """Delete an unpublished deposition (cleanup orphans)."""
        try:
            self._request("DELETE", f"/deposit/depositions/{deposition_id}")
            return True
        except ZenodoAPIError:
            return False

    def get_deposition(self, deposition_id: int) -> dict:
        """Get deposition status/details."""
        return self._request("GET", f"/deposit/depositions/{deposition_id}")

    def accept_community_requests(self, community_slug: str) -> int:
        """Accept all pending community inclusion requests.

        When you own the community and papers are submitted via the metadata
        communities field, they create 'submitted' requests that need acceptance.
        Returns the number of requests accepted.
        """
        # First get the community UUID
        try:
            community = self._request("GET", f"/communities/{community_slug}")
        except ZenodoAPIError:
            return 0
        community_id = community.get("id", "")

        # List open requests
        try:
            data = self._request(
                "GET",
                f"/requests?q=receiver.community:{community_id}&is_open=true&size=50"
            )
        except ZenodoAPIError:
            return 0

        hits = data.get("hits", {}).get("hits", [])
        accepted = 0
        for req_data in hits:
            accept_url = req_data.get("links", {}).get("actions", {}).get("accept")
            if accept_url:
                # Accept via full URL (not relative path)
                import urllib.request as _ur
                ar = _ur.Request(
                    accept_url, method="POST",
                    data=b"{}",
                    headers={
                        "Authorization": f"Bearer {self.token}",
                        "Content-Type": "application/json",
                    }
                )
                try:
                    with _ur.urlopen(ar, timeout=30, context=_ctx) as resp:
                        accepted += 1
                except Exception:
                    pass
        return accepted
