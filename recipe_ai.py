#!/usr/bin/env python3
"""MiMo Recipe AI - Generate recipes from ingredients."""
import os, argparse
from openai import OpenAI

client = OpenAI(api_key=os.getenv("MIMO_API_KEY"), base_url="https://api.xiaomimimo.com/v1")

def recipe(ingredients, cuisine="any"):
    r = client.chat.completions.create(model="mimo-v2.5", messages=[
        {"role": "system", "content": f"Chef AI. Cuisine: {cuisine}. Title, ingredients, steps, time."},
        {"role": "user", "content": f"Ingredients: {ingredients}"}])
    return r.choices[0].message.content

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("ingredients"); p.add_argument("--cuisine", default="any")
    a = p.parse_args(); print(recipe(a.ingredients, a.cuisine))
