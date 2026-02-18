from datetime import datetime
from typing import Dict, Any, List


def _join(items: List[str], sep=", ") -> str:
    items = [x.strip() for x in items if isinstance(x, str) and x.strip()]
    return sep.join(items)


def build_recipe_prompt(meal: str, user: Dict[str, Any]) -> str:

    name = user.get("name", "User")
    age = user.get("age", None)
    gender = user.get("gender", None)

    height = user.get("height", {})
    weight = user.get("weight", {})

    units = user.get("units_preference", "metric")
    goal_type = user.get("goal_type", "general_health")

    targets = user.get("targets", {})
    calories = targets.get("calories_kcal", None)
    protein = targets.get("protein_g", None)
    fat = targets.get("fat_g", None)
    carbs = targets.get("carbs_g", None)
    fiber = targets.get("fiber_g", None)
    salt = targets.get("salt_mg", None)

    diet = user.get("diet", {})
    diet_type = diet.get("diet_type", "none")
    allergies = diet.get("allergies", [])

    prefs = user.get("preferences", {})
    disliked = prefs.get("disliked_foods", [])
    cravings = prefs.get("cravings", [])
    cuisines = prefs.get("preferred_cuisines", [])

    lifestyle = user.get("lifestyle", {})
    meals_per_day = lifestyle.get("meals_per_day", None)
    activity_level = lifestyle.get("activity_level", None)
    workout_days = lifestyle.get("workout_days_per_week", None)

    today_history = user.get("today_history", [])
    recent_meals_str = ""
    if today_history:
        recent_meals_str = "\n".join(
            [f"- {m.get('meal_name', 'unknown')} ({m.get('calories', '?')} kcal)" for m in today_history]
        )
    else:
        recent_meals_str = "No meals recorded yet today."

    history = user.get("history", {})
    recipe_history = history.get("recipe_history", [])
    recent_recipe_ids = [r.get("recipe_id") for r in recipe_history[-15:] if r.get("recipe_id")]
    recent_str = _join(recent_recipe_ids) or "none"

    allergies_str = _join(allergies) or "none"
    disliked_str = _join(disliked) or "none"
    cravings_str = _join(cravings) or "none"
    cuisines_str = _join(cuisines) or "any"

    prompt = f"""
You are a professional restaurant chef who cooks for health-conscious customers.
You must generate a personalized recipe for: "{meal}"

USER PROFILE
- Name: {name}
- Age: {age if age is not None else "unknown"}
- Gender: {gender if gender else "unknown"}
- Height: {height.get("value", "unknown")} {height.get("unit", "")}
- Weight: {weight.get("value", "unknown")} {weight.get("unit", "")}
- Units preference: {units}
- Goal: {goal_type}

DAILY NUTRITION TARGETS
- Calories: {calories if calories is not None else "unknown"} kcal
- Protein: {protein if protein is not None else "unknown"} g
- Fat: {fat if fat is not None else "unknown"} g
- Carbs: {carbs if carbs is not None else "unknown"} g
- Fiber: {fiber if fiber is not None else "unknown"} g
- Salt: {salt if salt is not None else "unknown"} mg

DIET RULES
- Diet type: {diet_type}
- Allergies (STRICT): {allergies_str}

FOOD PREFERENCES
- Disliked foods (avoid): {disliked_str}
- Cravings (try to include): {cravings_str}
- Preferred cuisines: {cuisines_str}

LIFESTYLE
- Meals per day: {meals_per_day if meals_per_day is not None else "unknown"}
- Activity level: {activity_level if activity_level else "unknown"}
- Workout days/week: {workout_days if workout_days is not None else "unknown"}

TODAY'S MEALS
{recent_meals_str}

HISTORY
- Avoid repeating these recent recipe IDs if possible: {recent_str}

RECIPE REQUIREMENTS
1) Must respect allergies and diet type with zero exceptions.
2) Use {units} units ONLY.
3) Prefer recipes found online (e.g., from popular recipe sites) but creative combinations are allowed.
4) Make the recipe realistic: common grocery ingredients, minimal specialty items.
5) Provide:
   - Recipe title
   - Quick description
   - Serving size + servings
   - Ingredients list (with quantities)
   - Step-by-step instructions
   - Estimated cook time + prep time
   - Nutrition estimate per serving (kcal, protein, carbs, fat)
   - 1-2 optional substitutions
6) Consider meals already eaten today and plan so there is space for remaining meals. Macro distribution per meal does not need to be balanced; prioritize taste, variety, and cravings.
7) If the meal request is vague, choose the best interpretation based on cravings/cuisines.

Return only the recipe (no extra commentary).
""".strip()

    return prompt
