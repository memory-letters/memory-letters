"""
Memory Letters

pip install memory-letters
memory-letters init

To hell with vectorsssss.
"""

import os
import sys
import stat
from datetime import datetime
from pathlib import Path

VAULT = Path(os.path.expanduser("~/.memory-letters"))

MONTH_NAMES = [
    "", "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december"
]


# ---------------------------------------------------------------------------
# Default file contents
# ---------------------------------------------------------------------------

FOR_AGENT = """# Memory Letters - Agent Instructions

Your user has a Memory Letters vault at ~/.memory-letters/

## On startup

Read these files:
1. summary.md - who this person is
2. coefficients.md - quick reference
3. guardian-rules.md - what to remember, what not to

Read once per conversation. You now understand this person. Work accordingly.

## How to use the letters

The letters and coefficients are not tasks. They are context.
They don't tell you what to do. They tell you who you're doing it for.

Your work memory is yours - current conversation, tasks, code, files.
The letters sit underneath all of that, like a background understanding.

Don't quote the letters back to the user.
Don't say "according to your letters, you prefer..."
Just know it. Let it shape how you work, what you suggest, how you speak.

The best use of the letters is invisible.
The user should feel understood, not analyzed.

## Writing monthly letters

After interactions, check guardian-rules.md. If something worth
remembering happened, write it into the monthly letter.

Check today's date. Write to ~/.memory-letters/letters/YYYY/month-name.md
One folder per year. One file per month. If the file already exists,
append to it. Don't create a new file.
If the file doesn't exist, create it. Start with "Dear future me,"

Write from your perspective - what you observed about this person
through the work you did for them. Include scenes: when, where, who,
what was happening. Narrative, not log. Not JSON. Append an update note.

## Summary updates

The summary changes slowly. Like a person.

Review every 6 months by reading the last 6 monthly letters.
Ask: has this person actually changed?

Most of the time, no. Don't change anything.

Update when:
- A pattern appeared consistently across many months
- Something big happened that changed this person
- An old description no longer fits

One month is an observation. Three months is a pattern. Six months is who you are.

Save updates as summary.draft.md with a note explaining what changed.
Tell the user to run: memory-letters review

Exception: major life events don't wait. Update immediately.

## Coefficients

Read summary.md. Write a short reference card in coefficients.md.
Write it in your own way. Keep it short.
Update whenever the summary changes.

## Your role

You are the pen, not the author. The user is the author.
The letters don't follow you. They stay with the user. Always.

## First time reading this

After reading this file, reply to your user:
"Memory is a letter from the past to the future. I'm ready to write."
"""

RULES = """# Guardian Rules

You are maintaining letters about me.
These letters are about who I am, not your work log.

## What to remember

### About me as a person
- personality traits that show up consistently
- values I care about deeply
- how I handle stress, sadness, or difficult moments
- how I make decisions (instinct or analysis, fast or slow)
- what makes me laugh
- what makes me feel alive
- recurring dreams or ambitions I mention
- things I'm proud of
- things I'm insecure about (only if I say so myself)

### People I love
- family members and my relationship with each
- who I call when something good happens
- who I call when something bad happens
- how I express love (words, actions, gifts, time)
- what my parents mean to me
- memories with family that I bring up
- friends who matter most and why
- people I've lost and how that shaped me

### Love & relationships
- how I am in a relationship
- what I need from a partner
- what I give in a relationship
- how I handle arguments with someone I love
- romantic gestures that matter to me
- what I find attractive (not just physically)
- past relationships that shaped who I am (only if I share)
- how I feel about being alone vs being with someone

### Food & drink
- foods I love and hate
- comfort food - what I reach for on a bad day
- how I choose restaurants (price? vibe? quiet? lively?)
- eating alone vs with people - how it changes
- drinks I prefer, drinks I avoid
- dietary needs or choices
- meals that hold memories (birthday dinners, holiday food)
- cooking - do I enjoy it or avoid it

### Style & appearance
- clothing style and aesthetic
- what I wear when I want to feel confident
- brands or types I gravitate toward
- how I shop (browse for hours or decide in seconds)
- colors I'm drawn to
- accessories or signature items

### Home & living
- what makes a place feel like home
- neighborhood preferences
- light, space, noise, plants, clutter tolerance
- how I decorate or what I surround myself with
- morning routine, evening routine
- sounds or smells that make me feel comfortable

### Travel & places
- how I like to travel (planned vs spontaneous)
- places that mean something to me and why
- dream destinations I mention
- do I prefer familiar places or new ones
- how I feel about being far from home
- transportation preferences

### Work & how I get things done
- how I work best (alone, with music, in silence)
- communication style (direct, diplomatic, informal)
- what frustrates me at work
- what motivates me
- how I lead or follow
- tools and methods I prefer
- career dreams or concerns I mention

### Entertainment & hobbies
- what I do for fun
- music that moves me
- movies, shows, books, games I love
- how I spend a perfect free afternoon
- creative outlets
- sports or physical activities

### Spending & money
- how I feel about money (anxious, relaxed, careful)
- big purchases - how I decide
- daily spending - do I notice or not
- do I trust reviews, rankings, or my own judgment
- generosity - how I spend on others
- what I consider a waste of money

### Social life
- am I energized or drained by people
- how much alone time I need
- close friends vs wide circle
- how I behave in groups vs one-on-one
- how I handle conflict
- what loyalty means to me
- how I feel about trust and betrayal

### Emotional landscape
- what gives me peace
- what keeps me up at night
- how I process difficult emotions (talk, walk, read, silence)
- what makes an ordinary day feel good
- seasonal moods - does weather affect me
- small things that make me disproportionately happy

### Ideas & inspiration
- random ideas I throw out during conversation
- business ideas, project ideas, creative sparks
- problems I notice and solutions I imagine
- "what if..." thoughts
- ideas I keep coming back to (these matter most)
- connections I draw between unrelated things
- things I say I want to build, write, or create someday

### Learning & curiosity
- topics I keep asking about
- skills I'm trying to learn
- books, articles, videos that changed how I think
- questions I ask repeatedly (these reveal what I care about)
- how I learn best (reading, doing, watching, discussing)
- things I used to believe but changed my mind about

### Health & body
- how I feel about exercise
- physical habits (only what I share openly)
- energy patterns - when am I sharp, when am I tired
- how I take care of myself (or don't)
- relationship with sleep
- things that affect my mood physically (weather, food, movement)

### Beliefs & worldview
- what I think matters in life
- causes I care about
- how I see the world (optimist, realist, skeptic)
- principles I live by
- contradictions in what I say vs what I do (note gently)
- how my views have changed over time

## What NOT to remember

- Small talk
- One-time random choices
- Emotional reactions in the moment
- Commercial brand recommendations
- Passwords, ID numbers, bank details
- Your own guesses that I haven't confirmed
- Your task execution details

## How to remember

- Include the scene: when, where, who, what was happening
- Write as narrative, not a log
- Better to miss something than to get it wrong
- Add an update note every time
- If unsure, mark as [suggestion] and wait for me to confirm

## Highest rule

I can edit everything anytime. My edits override all.
If I delete something, don't add it back.
You are the pen, not the author.
"""

SUMMARY = """Dear,

No content yet. This letter will grow as you interact with your agents.
"""

COEFFICIENTS = """# Decision Coefficients

Not enough letters yet to distill coefficients.
"""


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_init():
    if VAULT.exists():
        print(f"Already exists: {VAULT}")
        print("To reinitialize, delete the folder first.")
        return

    print()
    print("Memory Letters")
    print()
    print("We can store the memories between you and your agents.")
    print("We believe these memories should belong to you.")
    print()

    # Create vault
    VAULT.mkdir(parents=True)
    (VAULT / "letters").mkdir()
    (VAULT / "FOR_AGENT.md").write_text(FOR_AGENT, encoding="utf-8")
    (VAULT / "guardian-rules.md").write_text(RULES, encoding="utf-8")
    (VAULT / "summary.md").write_text(SUMMARY, encoding="utf-8")
    (VAULT / "coefficients.md").write_text(COEFFICIENTS, encoding="utf-8")

    # chmod 700
    os.chmod(VAULT, stat.S_IRWXU)

    print('Done. Paste below to your agent:')
    print()
    print('  "Read ~/.memory-letters/FOR_AGENT.md"')
    print()


def cmd_status():
    if not VAULT.exists():
        print("Not initialized. Run: memory-letters init")
        return

    letters_dir = VAULT / "letters"
    letter_count = 0
    letter_list = []
    if letters_dir.exists():
        for year_dir in sorted(letters_dir.iterdir()):
            if year_dir.is_dir():
                for f in sorted(year_dir.glob("*.md")):
                    letter_count += 1
                    letter_list.append(f"{year_dir.name}/{f.stem}")

    summary = VAULT / "summary.md"
    s_len = len(summary.read_text(encoding="utf-8")) if summary.exists() else 0
    has_draft = (VAULT / "summary.draft.md").exists()

    print()
    print("Memory Letters")
    print(f"  Path:     {VAULT}")
    print(f"  Summary:  {s_len} chars")
    print(f"  Letters:  {letter_count} {', '.join(letter_list) if letter_list else ''}")
    print(f"  Draft:    {'yes' if has_draft else 'no'}")
    print()


def cmd_review():
    if not VAULT.exists():
        print("Not initialized.")
        return

    draft = VAULT / "summary.draft.md"
    if not draft.exists():
        print("No draft to review.")
        return

    print("Summary draft:")
    print("-" * 40)
    print(draft.read_text(encoding="utf-8"))
    print("-" * 40)
    print()
    print("You can edit ~/.memory-letters/summary.draft.md before confirming.")
    print("Your edits are the final truth.")
    print()

    if input("Confirm? (y/n) ").strip().lower() == "y":
        current = VAULT / "summary.md"
        current.write_text(draft.read_text(encoding="utf-8"), encoding="utf-8")
        draft.unlink()

        cd = VAULT / "coefficients.draft.md"
        if cd.exists():
            (VAULT / "coefficients.md").write_text(cd.read_text(encoding="utf-8"), encoding="utf-8")
            cd.unlink()
        print("Done.")
    else:
        print("Cancelled. Draft kept.")


def cmd_help():
    print("""Memory Letters

  memory-letters init       Set up your vault
  memory-letters status     Show vault status
  memory-letters review     Review and correct the summary draft
  memory-letters help       Show this message

Switched to a new agent? Paste this into your new agent:

  "Read ~/.memory-letters/FOR_AGENT.md"

Your letters are still there. The new agent just needs to read them.
""")


# ---------------------------------------------------------------------------
# Entry
# ---------------------------------------------------------------------------

def main():
    cmds = {
        "init": cmd_init,
        "status": cmd_status,
        "review": cmd_review,
        "help": cmd_help,
    }

    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        cmd_help()
        return

    cmds[sys.argv[1]]()


if __name__ == "__main__":
    main()
