#!/usr/bin/env python3
"""
Relay▸Launch Business Audit Framework — Score Calculator

A CLI tool that takes audit scores as input and generates a business health
report with overall score, category breakdowns, and priority recommendations.

Usage:
    Interactive mode (default):
        python audit-score-calculator.py

    Quick score mode (provide overall category scores directly):
        python audit-score-calculator.py --quick \\
            --operations 3.2 \\
            --digital 2.8 \\
            --revenue 3.5 \\
            --journey 2.9

    Detailed mode (enter individual sub-category scores interactively):
        python audit-score-calculator.py --detailed

    Export to file:
        python audit-score-calculator.py --quick \\
            --operations 3.2 --digital 2.8 --revenue 3.5 --journey 2.9 \\
            --output report.txt

    Custom weights:
        python audit-score-calculator.py --quick \\
            --operations 3.2 --digital 2.8 --revenue 3.5 --journey 2.9 \\
            --weight-operations 0.35 --weight-digital 0.10 \\
            --weight-revenue 0.30 --weight-journey 0.25

    With business name:
        python audit-score-calculator.py --quick \\
            --operations 3.2 --digital 2.8 --revenue 3.5 --journey 2.9 \\
            --business-name "Acme Consulting"
"""

import argparse
import sys
from datetime import date


# ---------------------------------------------------------------------------
# Audit Structure Definition
# ---------------------------------------------------------------------------

AUDIT_STRUCTURE = {
    "operations": {
        "name": "Operations",
        "default_weight": 0.30,
        "categories": {
            "workflow": {
                "name": "Workflow Efficiency",
                "weight": 0.25,
                "item_count": 10,
            },
            "documentation": {
                "name": "Documentation and SOPs",
                "weight": 0.20,
                "item_count": 10,
            },
            "tools": {
                "name": "Tool Utilization",
                "weight": 0.15,
                "item_count": 10,
            },
            "bottlenecks": {
                "name": "Bottleneck Identification",
                "weight": 0.20,
                "item_count": 10,
            },
            "capacity": {
                "name": "Capacity Planning",
                "weight": 0.20,
                "item_count": 10,
            },
        },
    },
    "digital": {
        "name": "Digital Presence",
        "default_weight": 0.15,
        "categories": {
            "website": {
                "name": "Website",
                "weight": 0.25,
                "item_count": 10,
            },
            "seo": {
                "name": "SEO",
                "weight": 0.20,
                "item_count": 10,
            },
            "social": {
                "name": "Social Media",
                "weight": 0.15,
                "item_count": 10,
            },
            "brand": {
                "name": "Brand Consistency",
                "weight": 0.15,
                "item_count": 8,
            },
            "content": {
                "name": "Content Strategy",
                "weight": 0.10,
                "item_count": 8,
            },
            "reputation": {
                "name": "Online Reputation",
                "weight": 0.15,
                "item_count": 8,
            },
        },
    },
    "revenue": {
        "name": "Revenue and Growth",
        "default_weight": 0.30,
        "categories": {
            "channels": {
                "name": "Revenue Channels and Diversification",
                "weight": 0.25,
                "item_count": 8,
            },
            "pricing": {
                "name": "Pricing Strategy",
                "weight": 0.20,
                "item_count": 8,
            },
            "acquisition": {
                "name": "Customer Acquisition and Sales Efficiency",
                "weight": 0.20,
                "item_count": 8,
            },
            "retention": {
                "name": "Retention and Customer Lifetime Value",
                "weight": 0.20,
                "item_count": 8,
            },
            "expansion": {
                "name": "Expansion and Growth Opportunities",
                "weight": 0.15,
                "item_count": 9,
            },
        },
    },
    "journey": {
        "name": "Customer Journey",
        "default_weight": 0.25,
        "categories": {
            "awareness": {
                "name": "Awareness",
                "weight": 0.15,
                "item_count": 7,
            },
            "consideration": {
                "name": "Consideration",
                "weight": 0.20,
                "item_count": 9,
            },
            "purchase": {
                "name": "Purchase",
                "weight": 0.15,
                "item_count": 6,
            },
            "onboarding": {
                "name": "Onboarding",
                "weight": 0.20,
                "item_count": 8,
            },
            "retention_delivery": {
                "name": "Retention and Value Delivery",
                "weight": 0.20,
                "item_count": 9,
            },
            "advocacy": {
                "name": "Advocacy",
                "weight": 0.10,
                "item_count": 7,
            },
        },
    },
}


# ---------------------------------------------------------------------------
# Rating Descriptions
# ---------------------------------------------------------------------------

HEALTH_RATINGS = [
    (1.0, 1.9, "CRISIS",
     "Foundational issues threaten business viability. Immediate intervention required."),
    (2.0, 2.4, "UNSTABLE (LOW)",
     "Multiple significant gaps creating compounding risk. Focused remediation needed."),
    (2.5, 2.9, "UNSTABLE (HIGH)",
     "The business functions but leaves substantial value on the table. "
     "Build systems to reduce reliance on heroic effort."),
    (3.0, 3.4, "DEVELOPING",
     "Core functions work but competitive disadvantages exist. "
     "Prioritize the two weakest categories."),
    (3.5, 3.9, "SOLID",
     "The business is well-run with specific optimization opportunities. "
     "Fine-tune and begin scaling."),
    (4.0, 4.4, "STRONG",
     "High-performing across most dimensions. Address remaining gaps and focus on scaling."),
    (4.5, 5.0, "OPTIMIZED",
     "Best-in-class execution. Shift focus to innovation and strategic growth."),
]

SCORE_LABELS = {
    1: "Critical Gap",
    2: "Significant Weakness",
    3: "Functional",
    4: "Strong",
    5: "Optimized",
}


# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------

def get_health_rating(score):
    """Return the rating label and description for a given score."""
    for low, high, label, description in HEALTH_RATINGS:
        if low <= score <= high:
            return label, description
    if score < 1.0:
        return "INVALID", "Score is below the minimum threshold."
    return "INVALID", "Score is above the maximum threshold."


def score_bar(score, width=20):
    """Generate a text-based progress bar for a score."""
    filled = int((score / 5.0) * width)
    empty = width - filled
    bar = "#" * filled + "-" * empty
    return "[{}] {:.1f}/5.0".format(bar, score)


def get_score_label(score):
    """Return the label for a rounded score."""
    rounded = max(1, min(5, round(score)))
    return SCORE_LABELS.get(rounded, "Unknown")


def validate_score(value, name="Score"):
    """Validate that a score is between 1.0 and 5.0."""
    if value < 1.0 or value > 5.0:
        print("  Warning: {} ({}) is outside the 1.0-5.0 range. "
              "Clamping.".format(name, value))
        return max(1.0, min(5.0, value))
    return value


def prompt_score(prompt_text):
    """Prompt the user for a score with validation."""
    while True:
        try:
            raw = input("  {} (1-5, or 's' to skip): ".format(prompt_text)).strip()
            if raw.lower() == "s":
                return None
            value = float(raw)
            if value < 1.0 or value > 5.0:
                print("    Score must be between 1.0 and 5.0. Try again.")
                continue
            return value
        except ValueError:
            print("    Invalid input. Enter a number between 1 and 5, "
                  "or 's' to skip.")
        except (EOFError, KeyboardInterrupt):
            print("\n\nAudit cancelled.")
            sys.exit(0)


def calculate_weighted_score(category_scores, categories):
    """Calculate weighted score from category scores and their definitions."""
    total_weight = 0.0
    weighted_sum = 0.0
    for key, score in category_scores.items():
        if score is not None and key in categories:
            weight = categories[key]["weight"]
            weighted_sum += score * weight
            total_weight += weight
    if total_weight == 0:
        return None
    return weighted_sum / total_weight


# ---------------------------------------------------------------------------
# Input Modes
# ---------------------------------------------------------------------------

def collect_quick_scores(args):
    """Collect scores from command-line arguments in quick mode."""
    audit_scores = {}
    for key in ["operations", "digital", "revenue", "journey"]:
        value = getattr(args, key, None)
        if value is not None:
            audit_scores[key] = validate_score(
                value, AUDIT_STRUCTURE[key]["name"]
            )
        else:
            audit_scores[key] = None
    return audit_scores


def collect_interactive_scores():
    """Collect audit-level scores interactively."""
    print("")
    print("=" * 60)
    print("  RELAY>LAUNCH BUSINESS AUDIT - SCORE ENTRY")
    print("=" * 60)
    print("")
    print("  Enter the overall score for each audit area (1.0 - 5.0).")
    print("  Press 's' to skip an audit that was not conducted.")
    print("")

    audit_scores = {}
    for key, audit in AUDIT_STRUCTURE.items():
        score = prompt_score("{}:".format(audit["name"]))
        audit_scores[key] = score

    return audit_scores


def collect_detailed_scores():
    """Collect individual category scores for each audit interactively."""
    print("")
    print("=" * 60)
    print("  RELAY>LAUNCH BUSINESS AUDIT - DETAILED SCORE ENTRY")
    print("=" * 60)
    print("")
    print("  Enter category scores for each audit area (1.0 - 5.0).")
    print("  Press 's' to skip a category.")
    print("")

    audit_scores = {}
    category_details = {}

    for audit_key, audit in AUDIT_STRUCTURE.items():
        print("\n  --- {} Audit ---".format(audit["name"]))

        skip_all = False
        try:
            skip_input = input("  Score this audit? (y/n): ").strip().lower()
            if skip_input == "n":
                skip_all = True
        except (EOFError, KeyboardInterrupt):
            print("\n\nAudit cancelled.")
            sys.exit(0)

        if skip_all:
            audit_scores[audit_key] = None
            continue

        cat_scores = {}
        for cat_key, cat in audit["categories"].items():
            score = prompt_score("  {}:".format(cat["name"]))
            cat_scores[cat_key] = score

        category_details[audit_key] = cat_scores
        weighted = calculate_weighted_score(cat_scores, audit["categories"])
        audit_scores[audit_key] = weighted

        if weighted is not None:
            print("\n  >> {} Weighted Score: {:.2f}".format(
                audit["name"], weighted
            ))

    return audit_scores, category_details


# ---------------------------------------------------------------------------
# Recommendation Engine
# ---------------------------------------------------------------------------

RECOMMENDATIONS = {
    "operations": {
        (1.0, 1.9): {
            "priority": "CRITICAL",
            "text": ("Operations are in crisis. Document the three most repeated "
                     "processes as SOPs this week. Assign clear ownership for "
                     "every active project."),
            "impact": "High - stabilizes daily execution",
        },
        (2.0, 2.9): {
            "priority": "HIGH",
            "text": ("Operational gaps are limiting growth. Implement a project "
                     "management system, document core workflows, and establish "
                     "a weekly team review cadence."),
            "impact": "High - reduces errors and unlocks capacity",
        },
        (3.0, 3.4): {
            "priority": "MEDIUM",
            "text": ("Operations are functional but have friction. Identify the "
                     "top three bottlenecks and build targeted solutions."),
            "impact": "Medium - improves efficiency and team satisfaction",
        },
        (3.5, 5.0): {
            "priority": "LOW",
            "text": ("Operations are solid. Focus on automation of repetitive "
                     "tasks and capacity planning for the next growth phase."),
            "impact": "Medium - prepares for scale",
        },
    },
    "digital": {
        (1.0, 1.9): {
            "priority": "CRITICAL",
            "text": ("Digital presence is nearly absent. Claim Google Business "
                     "Profile, ensure the website communicates what you do, and "
                     "pick one social platform to post on consistently."),
            "impact": "High - creates baseline visibility",
        },
        (2.0, 2.9): {
            "priority": "HIGH",
            "text": ("Digital presence has significant gaps. Fix website "
                     "performance and messaging, implement basic SEO, and "
                     "establish a review generation process."),
            "impact": "High - increases inbound lead flow",
        },
        (3.0, 3.4): {
            "priority": "MEDIUM",
            "text": ("Digital presence is adequate but not competitive. Develop "
                     "a content strategy, optimize for target keywords, and "
                     "build a lead capture system on the website."),
            "impact": "Medium - improves lead quality and volume",
        },
        (3.5, 5.0): {
            "priority": "LOW",
            "text": ("Digital presence is strong. Optimize conversion rates, "
                     "expand content reach, and test paid acquisition."),
            "impact": "Medium - scales existing momentum",
        },
    },
    "revenue": {
        (1.0, 1.9): {
            "priority": "CRITICAL",
            "text": ("Revenue model has critical vulnerabilities. Immediately "
                     "assess pricing against value delivered, identify "
                     "concentration risk, and calculate unit economics."),
            "impact": "High - threatens business viability",
        },
        (2.0, 2.9): {
            "priority": "HIGH",
            "text": ("Revenue growth is constrained. Review and raise pricing, "
                     "diversify away from client concentration, and implement "
                     "lead generation beyond referrals."),
            "impact": "High - directly increases revenue and reduces risk",
        },
        (3.0, 3.4): {
            "priority": "MEDIUM",
            "text": ("Revenue is growing but has structural weaknesses. Build "
                     "recurring revenue streams, implement retention tracking, "
                     "and create upsell paths."),
            "impact": "Medium - improves revenue predictability",
        },
        (3.5, 5.0): {
            "priority": "LOW",
            "text": ("Revenue engine is healthy. Focus on adjacent markets, "
                     "optimizing lifetime value, and building scalable offers."),
            "impact": "Medium - accelerates sustainable growth",
        },
    },
    "journey": {
        (1.0, 1.9): {
            "priority": "CRITICAL",
            "text": ("Customer journey is fragmented. Build a basic onboarding "
                     "process, establish regular client communication, and "
                     "create a follow-up sequence for leads."),
            "impact": "High - reduces churn and improves close rate",
        },
        (2.0, 2.9): {
            "priority": "HIGH",
            "text": ("Customer experience has significant gaps. Standardize "
                     "onboarding, implement satisfaction check-ins, and build "
                     "a referral request system."),
            "impact": "High - improves retention and generates referrals",
        },
        (3.0, 3.4): {
            "priority": "MEDIUM",
            "text": ("Customer journey works but has friction points. Map the "
                     "full journey, identify the two weakest stages, and build "
                     "specific improvements for each."),
            "impact": "Medium - increases satisfaction and advocacy",
        },
        (3.5, 5.0): {
            "priority": "LOW",
            "text": ("Customer journey is well-designed. Refine the advocacy "
                     "stage, systematize case studies, and build a loyalty "
                     "program."),
            "impact": "Medium - deepens customer relationships",
        },
    },
}


# Quick wins per area, used in 30/60/90-day plan generation
QUICK_WINS = {
    "operations": [
        "Document the top 3 most-repeated processes as written SOPs",
        "Implement a standard meeting agenda and action item template",
        "Audit current tool subscriptions and cancel unused ones",
    ],
    "digital": [
        "Claim and fully complete Google Business Profile",
        "Fix any broken links, missing images, or 404 errors on the website",
        "Set up a review request email sent after each completed project",
    ],
    "revenue": [
        "Raise prices 10-15% for all new clients starting this month",
        "Calculate customer acquisition cost for each marketing channel",
        "Identify top 5 clients by revenue and assess concentration risk",
    ],
    "journey": [
        "Create a welcome email template sent within 1 hour of signing",
        "Build a 5-email follow-up sequence for unconverted leads",
        "Implement a 30-day satisfaction check-in for new clients",
    ],
}

STRATEGIC_PROJECTS = {
    "operations": [
        "Implement or fully adopt a project management system across the team",
        "Build an employee/contractor onboarding checklist and documentation",
    ],
    "digital": [
        "Develop a 90-day content calendar targeting 5 priority keywords",
        "Build a lead magnet and email capture system on the website",
    ],
    "revenue": [
        "Design and launch a recurring revenue or retainer offer",
        "Build a formal sales pipeline with stages and conversion tracking",
    ],
    "journey": [
        "Design and document a standardized client onboarding process",
        "Implement quarterly business reviews with top 10 clients",
    ],
}

SUSTAINED_IMPROVEMENTS = {
    "operations": [
        "Conduct a full capacity planning exercise and define hiring triggers",
        "Establish monthly KPI review meetings with documented action items",
    ],
    "digital": [
        "Launch a monthly newsletter to nurture leads and stay top-of-mind",
        "Conduct a competitive analysis and refine positioning",
    ],
    "revenue": [
        "Build an upsell/cross-sell path for existing clients",
        "Implement customer lifetime value tracking and retention monitoring",
    ],
    "journey": [
        "Build a referral program with clear incentives and a simple process",
        "Create 3 detailed case studies from recent successful engagements",
    ],
}


def generate_recommendations(audit_scores, category_details=None):
    """Generate prioritized recommendations based on scores."""
    results = []

    # Sort by score ascending so worst areas come first
    sorted_scores = sorted(
        [(k, v) for k, v in audit_scores.items() if v is not None],
        key=lambda x: x[1],
    )

    for key, score in sorted_scores:
        if key not in RECOMMENDATIONS:
            continue
        for (low, high), rec in RECOMMENDATIONS[key].items():
            if low <= score <= high:
                results.append({
                    "area": AUDIT_STRUCTURE[key]["name"],
                    "priority": rec["priority"],
                    "text": rec["text"],
                    "impact": rec["impact"],
                })
                break

    # Add category-level callouts when detailed data is available
    if category_details:
        critical_cats = []
        for audit_key, cats in category_details.items():
            for cat_key, cat_score in cats.items():
                if cat_score is not None and cat_score < 2.5:
                    cat_name = (
                        AUDIT_STRUCTURE[audit_key]["categories"][cat_key]["name"]
                    )
                    audit_name = AUDIT_STRUCTURE[audit_key]["name"]
                    critical_cats.append((audit_name, cat_name, cat_score))

        critical_cats.sort(key=lambda x: x[2])
        for audit_name, cat_name, cat_score in critical_cats[:3]:
            results.append({
                "priority": "HIGH",
                "text": ("Category '{}' in {} scored {:.1f}. This is a "
                         "critical gap requiring immediate attention.".format(
                             cat_name, audit_name, cat_score)),
                "area": "{} > {}".format(audit_name, cat_name),
                "impact": "High - addresses a foundational weakness",
            })

    return results


def generate_day_plan(audit_scores):
    """Generate a 30/60/90-day focus plan based on scores."""
    plan = {"30": [], "60": [], "90": []}

    scored = {k: v for k, v in audit_scores.items() if v is not None}
    if not scored:
        plan["30"] = ["Complete audit scoring to generate action plan"]
        plan["60"] = ["Execute quick wins identified in audit"]
        plan["90"] = ["Begin strategic projects"]
        return plan

    sorted_scores = sorted(scored.items(), key=lambda x: x[1])
    weakest_key = sorted_scores[0][0]

    # 30-day quick wins from the weakest area
    plan["30"].extend(QUICK_WINS.get(weakest_key, []))
    if len(sorted_scores) > 1:
        second_key = sorted_scores[1][0]
        plan["30"].append(
            "Begin assessment of {} quick wins".format(
                AUDIT_STRUCTURE[second_key]["name"]
            )
        )

    # 60-day strategic projects from the two weakest areas
    plan["60"].extend(STRATEGIC_PROJECTS.get(weakest_key, []))
    if len(sorted_scores) > 1:
        second_key = sorted_scores[1][0]
        plan["60"].extend(STRATEGIC_PROJECTS.get(second_key, []))

    # 90-day sustained improvements
    plan["90"].extend(SUSTAINED_IMPROVEMENTS.get(weakest_key, []))
    if len(sorted_scores) > 1:
        second_key = sorted_scores[1][0]
        plan["90"].extend(SUSTAINED_IMPROVEMENTS.get(second_key, []))

    return plan


# ---------------------------------------------------------------------------
# Report Generation
# ---------------------------------------------------------------------------

def generate_report(audit_scores, weights, category_details=None,
                    business_name=None):
    """Generate the full business health report as a string."""
    lines = []

    # --- Header ---
    lines.append("")
    lines.append("=" * 64)
    lines.append("  RELAY>LAUNCH BUSINESS HEALTH REPORT")
    lines.append("=" * 64)
    if business_name:
        lines.append("  Business: {}".format(business_name))
    lines.append("  Date: {}".format(date.today().isoformat()))
    lines.append("  Framework: Business Audit Framework v1.0")
    lines.append("")

    # --- Calculate overall score ---
    total_weight = 0.0
    weighted_sum = 0.0
    scored_audits = {}

    for key, score in audit_scores.items():
        if score is not None:
            w = weights.get(key, AUDIT_STRUCTURE[key]["default_weight"])
            scored_audits[key] = {"score": score, "weight": w}
            weighted_sum += score * w
            total_weight += w

    if total_weight == 0:
        lines.append("  ERROR: No audit scores provided. Cannot generate report.")
        return "\n".join(lines)

    overall_score = weighted_sum / total_weight

    # --- Overall Score ---
    lines.append("-" * 64)
    lines.append("  OVERALL BUSINESS HEALTH SCORE")
    lines.append("-" * 64)
    lines.append("")

    rating_label, rating_desc = get_health_rating(overall_score)
    lines.append("  Score:  {:.2f} / 5.00".format(overall_score))
    lines.append("  Rating: {}".format(rating_label))
    lines.append("  {}".format(score_bar(overall_score, 30)))
    lines.append("")
    lines.append("  {}".format(rating_desc))
    lines.append("")

    # --- Audit Area Breakdown ---
    lines.append("-" * 64)
    lines.append("  AUDIT AREA BREAKDOWN")
    lines.append("-" * 64)
    lines.append("")

    sorted_audits = sorted(scored_audits.items(), key=lambda x: x[1]["score"])

    for key, data in sorted_audits:
        audit_name = AUDIT_STRUCTURE[key]["name"]
        score = data["score"]
        weight = data["weight"]
        label = get_score_label(score)
        lines.append("  {}".format(audit_name))
        lines.append("  {}".format(score_bar(score, 30)))
        lines.append("  Rating: {}  |  Weight: {:.0%}".format(label, weight))
        lines.append("")

    # --- Detailed Category Breakdown ---
    if category_details:
        lines.append("-" * 64)
        lines.append("  DETAILED CATEGORY BREAKDOWN")
        lines.append("-" * 64)
        lines.append("")

        for audit_key, cats in category_details.items():
            if not cats:
                continue
            audit_name = AUDIT_STRUCTURE[audit_key]["name"]
            lines.append("  {} Audit:".format(audit_name))
            lines.append("  {}".format("-" * 50))

            sorted_cats = sorted(
                [(k, v) for k, v in cats.items() if v is not None],
                key=lambda x: x[1],
            )

            for cat_key, cat_score in sorted_cats:
                cat_info = AUDIT_STRUCTURE[audit_key]["categories"][cat_key]
                cat_name = cat_info["name"]
                cat_weight = cat_info["weight"]
                lines.append("    {:<40} {:.1f}  (weight: {:.0%})".format(
                    cat_name, cat_score, cat_weight
                ))

            lines.append("")

    # --- Strengths and Weaknesses ---
    lines.append("-" * 64)
    lines.append("  STRENGTHS AND WEAKNESSES")
    lines.append("-" * 64)
    lines.append("")

    strengths = [(k, d) for k, d in sorted_audits if d["score"] >= 3.5]
    weaknesses = [(k, d) for k, d in sorted_audits if d["score"] < 3.0]
    middle = [(k, d) for k, d in sorted_audits
              if 3.0 <= d["score"] < 3.5]

    if strengths:
        lines.append("  STRENGTHS (3.5+):")
        for key, data in reversed(strengths):
            name = AUDIT_STRUCTURE[key]["name"]
            lines.append("    + {}: {:.1f}".format(name, data["score"]))
        lines.append("")

    if middle:
        lines.append("  DEVELOPING (3.0 - 3.4):")
        for key, data in middle:
            name = AUDIT_STRUCTURE[key]["name"]
            lines.append("    ~ {}: {:.1f}".format(name, data["score"]))
        lines.append("")

    if weaknesses:
        lines.append("  WEAKNESSES (below 3.0):")
        for key, data in weaknesses:
            name = AUDIT_STRUCTURE[key]["name"]
            lines.append("    - {}: {:.1f}".format(name, data["score"]))
        lines.append("")

    if not strengths and not weaknesses and not middle:
        lines.append("  No audit areas scored.")
        lines.append("")

    # --- Priority Recommendations ---
    lines.append("-" * 64)
    lines.append("  PRIORITY RECOMMENDATIONS")
    lines.append("-" * 64)
    lines.append("")

    recs = generate_recommendations(audit_scores, category_details)
    for i, rec in enumerate(recs, 1):
        lines.append("  {}. [{}] {}".format(i, rec["priority"], rec["text"]))
        lines.append("     Area: {}  |  Estimated Impact: {}".format(
            rec["area"], rec["impact"]
        ))
        lines.append("")

    # --- Gap Analysis ---
    lines.append("-" * 64)
    lines.append("  GAP ANALYSIS")
    lines.append("-" * 64)
    lines.append("")

    gap_score = 5.0 - overall_score
    lines.append("  Current Score:  {:.2f}".format(overall_score))
    lines.append("  Target Score:   5.00")
    lines.append("  Gap:            {:.2f}".format(gap_score))
    lines.append("")

    if overall_score < 3.0:
        milestone = 3.0
        lines.append("  Recommended first milestone: Reach 3.0 (Developing)")
        lines.append("  Points needed: {:.2f}".format(milestone - overall_score))
        lines.append("")
        lines.append("  Focus: Stabilize the weakest area first. A 1-point")
        lines.append("  improvement in the lowest-scoring audit area will have")
        lines.append("  the greatest effect on the overall score.")
    elif overall_score < 3.5:
        milestone = 3.5
        lines.append("  Recommended next milestone: Reach 3.5 (Solid)")
        lines.append("  Points needed: {:.2f}".format(milestone - overall_score))
        lines.append("")
        lines.append("  Focus: Address the weakest category within each audit")
        lines.append("  area. Moving two categories from 2.5 to 3.5 will shift")
        lines.append("  the overall score more than moving one from 3.5 to 5.0.")
    elif overall_score < 4.0:
        milestone = 4.0
        lines.append("  Recommended next milestone: Reach 4.0 (Strong)")
        lines.append("  Points needed: {:.2f}".format(milestone - overall_score))
        lines.append("")
        lines.append("  Focus: Optimize remaining weak spots and scale what")
        lines.append("  works. At this level, incremental improvements compound")
        lines.append("  quickly.")
    else:
        lines.append("  The business is performing well above average.")
        lines.append("  Focus: Maintain current standards, innovate, and expand.")
        lines.append("  Identify the one remaining gap with the highest")
        lines.append("  strategic value.")

    lines.append("")

    # --- 30/60/90-Day Plan ---
    lines.append("-" * 64)
    lines.append("  SUGGESTED 30/60/90-DAY FOCUS")
    lines.append("-" * 64)
    lines.append("")

    day_plan = generate_day_plan(audit_scores)

    lines.append("  DAYS 1-30 (Quick Wins):")
    for item in day_plan["30"]:
        lines.append("    * {}".format(item))
    lines.append("")
    lines.append("  DAYS 31-60 (Strategic Projects):")
    for item in day_plan["60"]:
        lines.append("    * {}".format(item))
    lines.append("")
    lines.append("  DAYS 61-90 (Sustained Improvement):")
    for item in day_plan["90"]:
        lines.append("    * {}".format(item))
    lines.append("")

    # --- Footer ---
    lines.append("=" * 64)
    lines.append("  Generated by Relay>Launch Business Audit Framework v1.0")
    lines.append("  {}".format(date.today().isoformat()))
    lines.append("=" * 64)
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI Entry Point
# ---------------------------------------------------------------------------

def build_parser():
    """Build the argument parser."""
    parser = argparse.ArgumentParser(
        prog="audit-score-calculator",
        description=(
            "Relay>Launch Business Audit Framework - Score Calculator. "
            "Generates a business health report from audit scores."
        ),
        epilog=(
            "Examples:\n"
            "  python audit-score-calculator.py\n"
            "  python audit-score-calculator.py --quick "
            "--operations 3.2 --digital 2.8 --revenue 3.5 --journey 2.9\n"
            "  python audit-score-calculator.py --detailed\n"
            "  python audit-score-calculator.py --quick "
            "--operations 3.2 --revenue 3.5 -n 'Acme Co' -o report.txt"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Mode selection
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        "--quick",
        action="store_true",
        help=("Quick mode: provide overall scores for each audit area "
              "via command-line arguments"),
    )
    mode_group.add_argument(
        "--detailed",
        action="store_true",
        help=("Detailed mode: enter individual category scores "
              "interactively"),
    )

    # Audit scores (for quick mode)
    score_group = parser.add_argument_group(
        "Audit Scores (for --quick mode)"
    )
    score_group.add_argument(
        "--operations", type=float, metavar="SCORE",
        help="Operations audit score (1.0 - 5.0)",
    )
    score_group.add_argument(
        "--digital", type=float, metavar="SCORE",
        help="Digital presence audit score (1.0 - 5.0)",
    )
    score_group.add_argument(
        "--revenue", type=float, metavar="SCORE",
        help="Revenue and growth audit score (1.0 - 5.0)",
    )
    score_group.add_argument(
        "--journey", type=float, metavar="SCORE",
        help="Customer journey audit score (1.0 - 5.0)",
    )

    # Custom weights
    weight_group = parser.add_argument_group(
        "Custom Weights (optional, must sum to 1.0)"
    )
    weight_group.add_argument(
        "--weight-operations", type=float, metavar="W",
        help="Weight for operations audit (default: 0.30)",
    )
    weight_group.add_argument(
        "--weight-digital", type=float, metavar="W",
        help="Weight for digital presence audit (default: 0.15)",
    )
    weight_group.add_argument(
        "--weight-revenue", type=float, metavar="W",
        help="Weight for revenue and growth audit (default: 0.30)",
    )
    weight_group.add_argument(
        "--weight-journey", type=float, metavar="W",
        help="Weight for customer journey audit (default: 0.25)",
    )

    # Output options
    parser.add_argument(
        "--output", "-o", type=str, metavar="FILE",
        help="Write report to a file instead of stdout",
    )
    parser.add_argument(
        "--business-name", "-n", type=str, metavar="NAME",
        help="Business name to include in the report header",
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    # --- Determine weights ---
    weights = {}
    custom_weights_provided = any([
        args.weight_operations,
        args.weight_digital,
        args.weight_revenue,
        args.weight_journey,
    ])

    if custom_weights_provided:
        weights = {
            "operations": (args.weight_operations
                           or AUDIT_STRUCTURE["operations"]["default_weight"]),
            "digital": (args.weight_digital
                        or AUDIT_STRUCTURE["digital"]["default_weight"]),
            "revenue": (args.weight_revenue
                        or AUDIT_STRUCTURE["revenue"]["default_weight"]),
            "journey": (args.weight_journey
                        or AUDIT_STRUCTURE["journey"]["default_weight"]),
        }
        total = sum(weights.values())
        if abs(total - 1.0) > 0.01:
            print("  Warning: Custom weights sum to {:.2f}, not 1.0. "
                  "Scores will be normalized.".format(total))
    else:
        for key, audit in AUDIT_STRUCTURE.items():
            weights[key] = audit["default_weight"]

    # --- Collect scores based on mode ---
    category_details = None

    if args.quick:
        audit_scores = collect_quick_scores(args)
        if not any(v is not None for v in audit_scores.values()):
            print("Error: --quick mode requires at least one audit score.")
            print("  Example: --quick --operations 3.2 --revenue 3.5")
            sys.exit(1)
    elif args.detailed:
        audit_scores, category_details = collect_detailed_scores()
    else:
        audit_scores = collect_interactive_scores()

    # --- Generate and output the report ---
    report = generate_report(
        audit_scores,
        weights,
        category_details=category_details,
        business_name=args.business_name,
    )

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(report)
            print("\n  Report saved to: {}".format(args.output))
        except IOError as e:
            print("  Error writing to {}: {}".format(args.output, e))
            sys.exit(1)
    else:
        print(report)


if __name__ == "__main__":
    main()
