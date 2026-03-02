#!/usr/bin/env python3
"""
Relay Launch — Business Audit Score Calculator

Takes audit scores as input and generates a business health report with
category breakdowns, overall score, and priority recommendations.

Usage:
    python audit-score-calculator.py
    python audit-score-calculator.py --interactive
    python audit-score-calculator.py --file scores.json
"""

import argparse
import json
import sys
from pathlib import Path


CATEGORIES = {
    "operations": {
        "name": "Operations & Process",
        "weight": 0.20,
        "items": [
            "Core workflows documented",
            "Bottlenecks identified and addressed",
            "Task management system in place",
            "Handoff processes defined",
            "Capacity planning exists",
            "Tools consolidated and integrated",
            "Quality control checkpoints exist",
            "Onboarding process documented",
        ],
    },
    "digital": {
        "name": "Digital Presence",
        "weight": 0.20,
        "items": [
            "Website is current and professional",
            "SEO fundamentals in place",
            "Google Business profile optimized",
            "Social media profiles active and consistent",
            "Brand messaging is clear and consistent",
            "Content strategy exists",
            "Online reviews are monitored",
            "Analytics tracking is configured",
        ],
    },
    "revenue": {
        "name": "Revenue & Growth",
        "weight": 0.20,
        "items": [
            "Revenue channels identified and tracked",
            "Pricing strategy is documented",
            "Customer acquisition cost is known",
            "Sales pipeline is defined",
            "Upsell and cross-sell paths exist",
            "Competitive positioning is clear",
            "New market opportunities evaluated",
            "Financial forecasting in place",
        ],
    },
    "customer": {
        "name": "Customer Journey",
        "weight": 0.20,
        "items": [
            "Customer touchpoints mapped",
            "Onboarding experience defined",
            "Feedback collection in place",
            "Support process documented",
            "Retention strategy exists",
            "Referral program or process exists",
            "Communication cadence defined",
            "Churn reasons tracked",
        ],
    },
    "team": {
        "name": "Team Systems",
        "weight": 0.10,
        "items": [
            "Communication tools standardized",
            "Meeting cadence and format defined",
            "Roles and responsibilities documented",
            "Knowledge base or wiki maintained",
            "Performance tracking in place",
        ],
    },
    "data": {
        "name": "Data & Reporting",
        "weight": 0.10,
        "items": [
            "KPIs defined and tracked",
            "Reporting cadence established",
            "Dashboard or tracking tool in use",
            "Data sources centralized",
            "Decisions reference data regularly",
        ],
    },
}

HEALTH_RATINGS = [
    (4.5, "Excellent", "Business is well-optimized. Focus on fine-tuning and scaling."),
    (3.5, "Strong", "Solid foundation. Targeted improvements will yield high returns."),
    (2.5, "Developing", "Clear opportunities to improve efficiency and revenue."),
    (1.5, "Needs Work", "Significant gaps in multiple areas. Prioritize highest-impact fixes."),
    (0.0, "Critical", "Fundamental systems are missing. Start with the basics."),
]


def get_health_rating(score):
    for threshold, label, description in HEALTH_RATINGS:
        if score >= threshold:
            return label, description
    return "Unknown", ""


def collect_scores_interactive():
    """Collect scores interactively from the terminal."""
    scores = {}
    print("\n" + "=" * 60)
    print("  RELAY LAUNCH — BUSINESS AUDIT SCORE CALCULATOR")
    print("=" * 60)
    print("\nRate each item from 1-5:")
    print("  1 = Critical Gap    2 = Weak    3 = Adequate")
    print("  4 = Strong          5 = Excellent")
    print("  0 = Not Applicable (skip)\n")

    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n--- {cat_data['name']} ---")
        cat_scores = []
        for item in cat_data["items"]:
            while True:
                try:
                    raw = input(f"  {item}: ")
                    score = int(raw.strip())
                    if score == 0:
                        break
                    if 1 <= score <= 5:
                        cat_scores.append({"item": item, "score": score})
                        break
                    print("    Enter a number 1-5 (or 0 to skip)")
                except (ValueError, EOFError):
                    print("    Enter a number 1-5 (or 0 to skip)")
        scores[cat_key] = cat_scores
    return scores


def load_scores_from_file(filepath):
    """Load scores from a JSON file."""
    path = Path(filepath)
    if not path.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    with open(path) as f:
        return json.load(f)


def calculate_results(scores):
    """Calculate category averages and overall score."""
    results = {}
    for cat_key, cat_data in CATEGORIES.items():
        cat_scores = scores.get(cat_key, [])
        if not cat_scores:
            continue
        score_values = [s["score"] for s in cat_scores]
        avg = sum(score_values) / len(score_values)
        low_items = [s for s in cat_scores if s["score"] <= 2]
        results[cat_key] = {
            "name": cat_data["name"],
            "weight": cat_data["weight"],
            "average": round(avg, 1),
            "item_count": len(score_values),
            "low_items": low_items,
        }

    if not results:
        return results, 0.0

    total_weight = sum(r["weight"] for r in results.values())
    overall = sum(r["average"] * r["weight"] for r in results.values()) / total_weight
    return results, round(overall, 1)


def generate_report(results, overall_score):
    """Generate a text-based audit report."""
    rating, rating_desc = get_health_rating(overall_score)

    lines = []
    lines.append("")
    lines.append("=" * 60)
    lines.append("  BUSINESS HEALTH REPORT")
    lines.append("  Generated by Relay Launch Audit Framework")
    lines.append("=" * 60)

    # Overall score
    bar_filled = int(overall_score * 10)
    bar_empty = 50 - bar_filled
    bar = "#" * bar_filled + "-" * bar_empty
    lines.append(f"\n  OVERALL SCORE: {overall_score} / 5.0  [{bar}]")
    lines.append(f"  HEALTH RATING: {rating}")
    lines.append(f"  {rating_desc}")

    # Category breakdown
    lines.append("\n" + "-" * 60)
    lines.append("  CATEGORY BREAKDOWN")
    lines.append("-" * 60)

    sorted_cats = sorted(results.values(), key=lambda x: x["average"])
    for cat in sorted_cats:
        cat_bar_filled = int(cat["average"] * 10)
        cat_bar = "#" * cat_bar_filled + "-" * (50 - cat_bar_filled)
        lines.append(f"\n  {cat['name']}")
        lines.append(f"  Score: {cat['average']} / 5.0  [{cat_bar}]")
        lines.append(f"  Items scored: {cat['item_count']}")
        if cat["low_items"]:
            lines.append(f"  Needs attention ({len(cat['low_items'])} items):")
            for item in cat["low_items"]:
                lines.append(f"    - {item['item']} (scored {item['score']})")

    # Priority recommendations
    all_low = []
    for cat in results.values():
        for item in cat["low_items"]:
            all_low.append({"category": cat["name"], **item})
    all_low.sort(key=lambda x: x["score"])

    if all_low:
        lines.append("\n" + "-" * 60)
        lines.append("  PRIORITY RECOMMENDATIONS")
        lines.append("-" * 60)
        lines.append("\n  Items scoring 1-2 (ordered by urgency):\n")
        for i, item in enumerate(all_low[:10], 1):
            lines.append(f"  {i}. [{item['category']}] {item['item']} — scored {item['score']}")

    # Next steps
    lines.append("\n" + "-" * 60)
    lines.append("  NEXT STEPS")
    lines.append("-" * 60)
    if overall_score >= 3.5:
        lines.append("\n  Your business has a strong foundation. Focus on:")
        lines.append("  - Addressing the specific low-scoring items above")
        lines.append("  - Automating repetitive processes")
        lines.append("  - Building dashboards for ongoing monitoring")
    elif overall_score >= 2.5:
        lines.append("\n  There are clear opportunities for improvement. We recommend:")
        lines.append("  - Tackling the top 3 quick wins immediately")
        lines.append("  - Building a 90-day improvement roadmap")
        lines.append("  - Documenting core processes as SOPs")
    else:
        lines.append("\n  Foundational work is needed. Start with:")
        lines.append("  - Picking the ONE highest-impact area and fixing it first")
        lines.append("  - Documenting your most critical process")
        lines.append("  - Setting up basic tracking and reporting")

    lines.append(f"\n  Want help? Submit a project request at:")
    lines.append(f"  https://github.com/Relay-Launch/Main/issues/new?template=project-request.yml")
    lines.append("\n" + "=" * 60)
    lines.append("")

    return "\n".join(lines)


def generate_sample_file():
    """Generate a sample scores JSON file."""
    sample = {}
    for cat_key, cat_data in CATEGORIES.items():
        sample[cat_key] = [
            {"item": item, "score": 3} for item in cat_data["items"]
        ]
    print(json.dumps(sample, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description="Relay Launch — Business Audit Score Calculator"
    )
    parser.add_argument(
        "--interactive", action="store_true",
        help="Collect scores interactively via prompts"
    )
    parser.add_argument(
        "--file", type=str,
        help="Load scores from a JSON file"
    )
    parser.add_argument(
        "--sample", action="store_true",
        help="Print a sample scores JSON file and exit"
    )
    args = parser.parse_args()

    if args.sample:
        generate_sample_file()
        return

    if args.file:
        scores = load_scores_from_file(args.file)
    elif args.interactive:
        scores = collect_scores_interactive()
    else:
        parser.print_help()
        print("\nExamples:")
        print("  python audit-score-calculator.py --interactive")
        print("  python audit-score-calculator.py --file scores.json")
        print("  python audit-score-calculator.py --sample > scores.json")
        return

    results, overall_score = calculate_results(scores)
    if not results:
        print("No scores provided. Nothing to calculate.")
        return

    report = generate_report(results, overall_score)
    print(report)


if __name__ == "__main__":
    main()
