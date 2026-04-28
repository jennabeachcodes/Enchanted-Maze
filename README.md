# Enchanted Maze

A Python text-based adventure game where players navigate a 3×3 grid world, explore unique environments, and collect hidden items before finding the exit portal.

---

## Gameplay Overview

You are dropped into an enchanted forest at the start of a maze. Navigate through varied landscapes, from dark caves and volcanic wastelands to canyon floors and grassy plains, collecting treasures along the way. Find the exit portal to end your adventure and see what you've gathered.

---

## World Map

```
        West ◄──────────────────────────────► East

        0,0              1,0              2,1
  N  ┌─────────────┬─────────────┬─────────────┐
  o  │  Enchanted  │  Grassy     │  Volcanic   │
  r  │  Forest     │  Foothills  │  Wasteland  │
  t  │  [START]    │             │             │
  h  ├─────────────┼─────────────┼─────────────┤
     │  Dark       │  Deep       │  Grass      │
     │  Cave       │  Canyon     │  Plains     │
     │  (DANGER)   │             │  [EXIT ->]  │
     ├─────────────┼─────────────┼─────────────┤
     │  BLOCKED    │  Swamp      │             │
  S  │  (Gruethorn)│             │             │
  o  └─────────────┴─────────────┴─────────────┘
  u
  t        0,1              1,1              1,2 / 2,2
  h
```

| Coordinates | Location | Item Available |
|---|---|---|
| 0,0 | Enchanted Forest | Treasure (hollow tree) |
| 1,0 | Grassy Foothills | Watch |
| 1,1 | Deep Canyon | Golden Top Hat |
| 1,2 | Swamp | Jeweled Skull |
| 2,1 | Volcanic Wasteland | Diamond |
| 2,2 | Grass Plains | Pot of Gold |
| 0,1 | Dark Cave | Danger — Gruethorn creature |

---

## Collectible Items

| Item | Location | How to Find |
|---|---|---|
| Treasure | 0,0 Enchanted Forest | Reach inside a hollow tree |
| Watch | 1,0 Grassy Foothills | Search the area |
| Golden Top Hat | 1,1 Deep Canyon | Search the area |
| Jeweled Skull | 1,2 Swamp | Search the area |
| Diamond | 2,1 Volcanic Wasteland | Search a pile of ash |
| Pot of Gold | 2,2 Grass Plains | Investigate a shiny glint in the grass |

Each item can only be collected once — once taken, it is removed from the world permanently.

---

## Requirements

- Python 3.6+
- No external dependencies

---

## How to Run

```bash
python gameFile.py
```

You will be prompted to enter your character's name, then the game begins at coordinates `0,0`.

---

## File Structure

| File | Purpose |
|---|---|
| `gameFile.py` | Entry point: launches the game and prompts for player name |
| `map.py` | All location logic and navigation between grid coordinates |
| `inventory.py` | Item definitions, world/player item lists, and item pickup functions |
| `menu.py` | Displays the in-game action menu |
| `directionsMenu.py` | Displays the available movement directions |

---

## Controls

At each location, press the corresponding number and hit Enter:

| Key | Action |
|---|---|
| `1` | Look around - describes your surroundings |
| `2` | Move - prompts for a direction |
| `3` | Take an object - attempts to pick up any item present |
| `4` | Directions - lists available compass directions |
| `0` | Exit game |

When moving, type a compass direction (e.g. `North`, `N`, `south`, `s` not case-sensitive).

---

## Special Locations

**Dark Cave (0,1):** Moving south, east, or west will trigger a deadly Gruethorn encounter. Only moving north is safe.

**Portal (1,2 - west wall):** A mysterious portal that transports you back to the start at `0,0`.

**Chasm (2,2 - east):** Jumping in ends the game immediately.

**Exit Portal (2,2 - south):** Walk through to end the game and view your final inventory.

---

## Ending the Game

Navigate to `2,2` (Grass Plains) and move **South** to find the glowing exit portal. Your final inventory will be displayed, showing every item you collected throughout your journey.

---

## Licence

This project is provided for educational purposes only as part of course work for Computer Programming at Algonquin College, Ottawa, ON, Canada.
