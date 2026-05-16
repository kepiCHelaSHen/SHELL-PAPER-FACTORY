#!/bin/bash
# Run v2 external reviews on all 6 papers via GPT-4o and Grok-3
# Fires all 12 calls, 2 at a time (one GPT + one Grok per paper)

REVIEW_PROMPT=$(cat /c/PROJECTS/SHELL/prompts/09_external_review.md | sed 's/\[PASTE PAPER HERE\]//' )

PAPERS=(
  "DRUG_SPENDING_2026_2026-05-15_003"
  "HOSPITAL_PRICING_2026_2026-05-15_003"
  "OPIOID_PRESCRIBING_2026_2026-05-15_003"
  "REPLICATION_CRISIS_2026_2026-05-15_003"
  "TECH_LOCKIN_2026_2026-05-15_003"
  "VACCINE_GAME_2026_2026-05-15_002"
)

DATE=$(date +%Y-%m-%d)

call_openai() {
  local slug=$1
  local paper_path="/c/PROJECTS/SHELL/papers/$slug/best_paper.md"
  local out_path="/c/PROJECTS/SHELL/papers/$slug/reviews/GPT4o_review_${DATE}.md"

  local paper_content=$(cat "$paper_path")
  local full_prompt="$REVIEW_PROMPT

---

$paper_content"

  local escaped=$(python3 -c "import json,sys; print(json.dumps(sys.stdin.read()))" <<< "$full_prompt")

  local response=$(curl -s --max-time 300 https://api.openai.com/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d "{
      \"model\": \"gpt-4o\",
      \"messages\": [{\"role\": \"user\", \"content\": $escaped}],
      \"temperature\": 0.3,
      \"max_tokens\": 8192
    }")

  echo "$response" | python3 -c "import json,sys; r=json.load(sys.stdin); print(r.get('choices',[{}])[0].get('message',{}).get('content','ERROR: '+json.dumps(r)))" > "$out_path"
  echo "GPT4o done: $slug"
}

call_grok() {
  local slug=$1
  local paper_path="/c/PROJECTS/SHELL/papers/$slug/best_paper.md"
  local out_path="/c/PROJECTS/SHELL/papers/$slug/reviews/Grok3_review_${DATE}.md"

  local paper_content=$(cat "$paper_path")
  local full_prompt="$REVIEW_PROMPT

---

$paper_content"

  local escaped=$(python3 -c "import json,sys; print(json.dumps(sys.stdin.read()))" <<< "$full_prompt")

  local response=$(curl -s --max-time 300 https://api.x.ai/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $XAI_API_KEY" \
    -d "{
      \"model\": \"grok-3-latest\",
      \"messages\": [{\"role\": \"user\", \"content\": $escaped}],
      \"temperature\": 0.3,
      \"max_tokens\": 8192
    }")

  echo "$response" | python3 -c "import json,sys; r=json.load(sys.stdin); print(r.get('choices',[{}])[0].get('message',{}).get('content','ERROR: '+json.dumps(r)))" > "$out_path"
  echo "Grok3 done: $slug"
}

echo "Starting 12 reviews at $(date)"
echo "================================"

# Fire all 12 in background, but stagger slightly to avoid burst rate limits
for slug in "${PAPERS[@]}"; do
  call_openai "$slug" &
  call_grok "$slug" &
  sleep 2  # small stagger between paper pairs
done

# Wait for all
wait
echo "================================"
echo "All 12 reviews complete at $(date)"
