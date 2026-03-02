# KPI Selection Guide

**By Relay▸Launch** | Choosing the Right Metrics for Your Business

---

## How to Use This Guide

Find your industry below and start with the KPIs marked as **Core**. These are the metrics that virtually every business in your category should track from day one. The ones marked as **Growth** become important as you scale past the initial stage and need more granular visibility.

**Golden rule:** Start with 5-8 KPIs. Track them consistently for 90 days before adding more. A small set of metrics you actually review every week will outperform a sprawling dashboard that no one looks at.

For each KPI, we provide:
- **Definition** — What it measures and why it matters
- **Formula** — How to calculate it
- **Target guidance** — What "good" looks like (varies by context, but gives you a starting point)
- **Review cadence** — How often you should look at this number

---

## SaaS (Software as a Service)

SaaS businesses live and die by retention and growth efficiency. Your dashboard should answer two questions every week: "Are we growing efficiently?" and "Are we keeping the customers we have?"

### Core Metrics

#### 1. Monthly Recurring Revenue (MRR)

- **Definition:** The total predictable revenue normalized to a monthly amount. This is the heartbeat of any SaaS business. If you track only one number, track this.
- **Formula:** `SUM(all active subscription amounts normalized to monthly)`
- **Breakdown components:**
  - New MRR = revenue from new customers this month
  - Expansion MRR = upgrades and add-ons from existing customers
  - Contraction MRR = downgrades from existing customers
  - Churned MRR = revenue lost from canceled customers
  - Net New MRR = New + Expansion - Contraction - Churned
- **Target guidance:** Net New MRR should be positive every month. Healthy SaaS businesses grow MRR 10-20% month-over-month in early stages, 5-10% in growth stage.
- **Review cadence:** Weekly (with monthly deep dive into components)

#### 2. Customer Churn Rate

- **Definition:** The percentage of customers who cancel or fail to renew in a given period. High churn is the silent killer of SaaS businesses because it compounds.
- **Formula:** `(Customers lost during period / Customers at start of period) x 100`
- **Target guidance:** Monthly churn below 3% for SMB-focused products, below 1% for enterprise. Annual churn below 10% is considered strong.
- **Review cadence:** Monthly (with a quarterly cohort analysis)

#### 3. Revenue Churn Rate (Net Revenue Retention)

- **Definition:** The percentage of revenue retained from existing customers, including expansion. This is more important than customer churn because it accounts for upsells offsetting losses.
- **Formula:** `((MRR at start of month - Churned MRR - Contraction MRR + Expansion MRR) / MRR at start of month) x 100`
- **Target guidance:** Above 100% means your existing customers are worth more over time (expansion exceeds churn). Best-in-class SaaS companies achieve 110-130% net revenue retention.
- **Review cadence:** Monthly

#### 4. Customer Acquisition Cost (CAC)

- **Definition:** How much you spend to acquire one new customer. Includes all sales and marketing costs.
- **Formula:** `(Total sales + marketing spend in period) / Number of new customers acquired in period`
- **Target guidance:** Depends entirely on your price point. The meaningful metric is the CAC ratio (see LTV:CAC below).
- **Review cadence:** Monthly

#### 5. Lifetime Value (LTV)

- **Definition:** The total revenue you expect to earn from a customer over the entire relationship.
- **Formula:** `Average Revenue Per Account (ARPA) x Gross Margin % x (1 / Monthly Churn Rate)`
- **Simplified version:** `ARPA x Average Customer Lifespan in Months x Gross Margin %`
- **Target guidance:** LTV:CAC ratio should be at least 3:1. Below 3:1 means you are spending too much to acquire customers relative to their value. Above 5:1 may mean you are under-investing in growth.
- **Review cadence:** Quarterly (this is a slow-moving metric)

#### 6. MRR Growth Rate

- **Definition:** The month-over-month percentage change in MRR. Shows trajectory and momentum.
- **Formula:** `((MRR this month - MRR last month) / MRR last month) x 100`
- **Target guidance:** Varies by stage. Pre-product-market-fit: volatile and acceptable. Post-PMF: aim for consistent positive growth. The T2D3 framework (triple, triple, double, double, double annual revenue) is a common VC benchmark.
- **Review cadence:** Monthly

### Growth Metrics

#### 7. CAC Payback Period

- **Definition:** How many months it takes to recoup the cost of acquiring a customer. This is a cash flow metric as much as a profitability metric.
- **Formula:** `CAC / (ARPA x Gross Margin %)`
- **Target guidance:** Under 12 months for SMB SaaS, under 18 months for mid-market, under 24 months for enterprise.
- **Review cadence:** Quarterly

#### 8. Activation Rate

- **Definition:** The percentage of new signups that reach a predefined "activated" state (completed onboarding, used a core feature, invited a team member, etc.). If this number is low, nothing else matters.
- **Formula:** `(Users who hit activation milestone / Total new signups) x 100`
- **Target guidance:** Define your activation event first. Then aim for 40-60% for self-serve products, 70-90% for sales-assisted onboarding.
- **Review cadence:** Weekly

#### 9. Monthly Active Users (MAU) / Daily Active Users (DAU)

- **Definition:** The number of unique users who engage with your product in a given period. DAU/MAU ratio indicates stickiness.
- **Formula:** `Count of unique users with at least one session in period`
- **Target guidance:** DAU/MAU ratio above 20% is considered good for most B2B SaaS. Above 50% indicates high daily engagement (messaging apps, project management tools).
- **Review cadence:** Weekly

#### 10. Average Revenue Per Account (ARPA)

- **Definition:** Revenue per customer on average. Tracks whether you are moving upmarket or down.
- **Formula:** `Total MRR / Total number of active accounts`
- **Target guidance:** Should trend upward over time through better packaging, pricing, and expansion.
- **Review cadence:** Monthly

#### 11. Quick Ratio (SaaS)

- **Definition:** Measures growth efficiency by comparing revenue additions to revenue losses. A high quick ratio means you are growing despite churn.
- **Formula:** `(New MRR + Expansion MRR) / (Churned MRR + Contraction MRR)`
- **Target guidance:** Above 4.0 is excellent. Above 2.0 is healthy. Below 1.0 means you are shrinking.
- **Review cadence:** Monthly

#### 12. Support Ticket Volume & Resolution Time

- **Definition:** Leading indicators of product health and customer satisfaction. Spikes often precede churn increases.
- **Formula:** `Count of new tickets per period` and `Average time from ticket creation to resolution`
- **Target guidance:** Median resolution time under 4 hours for critical issues, under 24 hours for standard. Volume should decrease relative to user base over time.
- **Review cadence:** Weekly

---

## E-Commerce

E-commerce KPIs revolve around traffic, conversion, and unit economics. Your dashboard should answer: "Are we turning traffic into profitable orders, and are customers coming back?"

### Core Metrics

#### 1. Revenue

- **Definition:** Total gross revenue from orders. Obvious, but track it in the right segments: by channel, by product category, by customer type (new vs. returning).
- **Formula:** `SUM(order totals) for the period`
- **Target guidance:** Context-dependent. Track month-over-month and year-over-year growth rates.
- **Review cadence:** Daily

#### 2. Conversion Rate

- **Definition:** The percentage of site visitors who complete a purchase. The single most leverageable metric in e-commerce.
- **Formula:** `(Number of orders / Number of unique sessions) x 100`
- **Target guidance:** Average e-commerce conversion rate is 2-3%. Above 3.5% is strong. Above 5% is exceptional. Varies significantly by category (luxury goods convert lower, consumables convert higher).
- **Review cadence:** Daily

#### 3. Average Order Value (AOV)

- **Definition:** The average dollar amount per transaction. Increasing AOV is often easier than increasing traffic or conversion rate.
- **Formula:** `Total revenue / Number of orders`
- **Target guidance:** Benchmark against your category. Focus on trend direction. Cross-sells, bundles, and free shipping thresholds are the standard levers.
- **Review cadence:** Weekly

#### 4. Customer Acquisition Cost (CAC)

- **Definition:** Total cost to acquire a new customer including ad spend, agency fees, discounts, and promotional costs.
- **Formula:** `Total acquisition spend / Number of new customers`
- **Target guidance:** Must be lower than your first-order profit for single-purchase businesses. For businesses with repeat purchases, compare to LTV.
- **Review cadence:** Weekly (by channel)

#### 5. Cart Abandonment Rate

- **Definition:** The percentage of shoppers who add items to their cart but do not complete the purchase. The most actionable metric for quick revenue recovery.
- **Formula:** `(1 - (Completed orders / Shopping carts created)) x 100`
- **Target guidance:** Average is around 70%. Getting this below 60% through checkout optimization, abandoned cart emails, and payment options is achievable.
- **Review cadence:** Weekly

#### 6. Return Rate

- **Definition:** The percentage of orders returned. Directly impacts profitability and is often overlooked in top-line metrics.
- **Formula:** `(Number of returned orders / Total orders) x 100`
- **Target guidance:** Varies wildly by category. Apparel: 20-30% is normal. Electronics: 5-10%. Food: below 2%. Track trend, not just absolute number.
- **Review cadence:** Monthly

### Growth Metrics

#### 7. Customer Lifetime Value (CLV)

- **Definition:** Total expected revenue from a customer across all future purchases.
- **Formula:** `AOV x Average purchase frequency x Average customer lifespan`
- **More precise:** Use cohort-based calculation tracking actual revenue per customer cohort over time
- **Target guidance:** CLV:CAC ratio of 3:1 or better. Below 2:1 indicates a problem with either acquisition cost or retention.
- **Review cadence:** Quarterly

#### 8. Repeat Purchase Rate

- **Definition:** The percentage of customers who make more than one purchase. This is the leading indicator of a sustainable e-commerce business.
- **Formula:** `(Customers with 2+ orders / Total customers) x 100`
- **Target guidance:** 25-30% is typical. Above 40% is strong. Subscription models should aim for 60%+.
- **Review cadence:** Monthly

#### 9. Revenue Per Visitor (RPV)

- **Definition:** Combines conversion rate and AOV into a single efficiency metric. Useful for comparing channels and time periods.
- **Formula:** `Total revenue / Number of unique visitors`
- **Target guidance:** Track trend over time. Use this to compare marketing channels on equal footing.
- **Review cadence:** Weekly

#### 10. Inventory Turnover

- **Definition:** How quickly you sell through inventory. Low turnover ties up cash. High turnover risks stockouts.
- **Formula:** `Cost of goods sold / Average inventory value`
- **Target guidance:** 4-6 turns per year for general merchandise. Higher for perishables. Lower for luxury or specialty items.
- **Review cadence:** Monthly

#### 11. Gross Margin

- **Definition:** Revenue minus the direct cost of goods sold, expressed as a percentage. The floor beneath all your other economics.
- **Formula:** `((Revenue - COGS) / Revenue) x 100`
- **Target guidance:** 40-60% for most e-commerce. Below 30% makes profitability very difficult after marketing and operations costs.
- **Review cadence:** Monthly (by product category)

#### 12. Email Revenue Percentage

- **Definition:** The share of total revenue driven by email marketing. A healthy email channel reduces dependence on paid acquisition.
- **Formula:** `(Revenue attributed to email / Total revenue) x 100`
- **Target guidance:** 20-30% of total revenue for mature e-commerce operations. Below 10% means you are likely over-reliant on paid channels.
- **Review cadence:** Weekly

---

## Professional Services

Professional services firms (consulting, agencies, law, accounting, engineering) sell time. Your dashboard should answer: "Are we selling enough time at the right rates, and are we delivering profitably?"

### Core Metrics

#### 1. Billable Utilization Rate

- **Definition:** The percentage of available hours that are billed to clients. This is the most important metric for any professional services firm. A 5% improvement in utilization typically drops more to the bottom line than a 5% increase in rates.
- **Formula:** `(Billable hours / Total available hours) x 100`
- **Total available hours** = working days in period x hours per day (typically 8) x number of staff
- **Target guidance:** 65-75% for consulting firms. 60-70% for agencies (account for internal creative work). 70-80% for accounting and legal. 100% is not the goal — you need time for business development, training, and administration.
- **Review cadence:** Weekly

#### 2. Effective Bill Rate

- **Definition:** The actual revenue earned per hour of work, accounting for write-downs, fixed-fee overruns, and discounts. The gap between your standard rate and effective rate tells you how much revenue you are leaving on the table.
- **Formula:** `Total revenue recognized / Total billable hours worked`
- **Target guidance:** Should be within 85-95% of your standard billing rate. Below 80% indicates scoping, estimation, or pricing problems.
- **Review cadence:** Monthly (by client, by project type)

#### 3. Revenue Per Employee

- **Definition:** Total revenue divided by headcount. A high-level measure of firm productivity and a useful benchmark against industry peers.
- **Formula:** `Total revenue / Number of full-time equivalent employees`
- **Target guidance:** $150K-$250K for general consulting. $200K-$400K for specialized or technical consulting. $100K-$180K for marketing agencies.
- **Review cadence:** Quarterly

#### 4. Project Profit Margin

- **Definition:** The profitability of individual client engagements after direct labor and expenses.
- **Formula:** `((Project revenue - Direct labor cost - Direct expenses) / Project revenue) x 100`
- **Target guidance:** 30-50% for consulting. 20-40% for agencies. Below 20% on a project usually means a scoping or estimation failure.
- **Review cadence:** At project completion, with monthly in-progress reviews for long engagements

#### 5. Pipeline Value

- **Definition:** Total potential revenue from active proposals and opportunities weighted by probability of close.
- **Formula:** `SUM(opportunity value x probability of winning) for all active opportunities`
- **Target guidance:** Weighted pipeline should be 3-4x your revenue target for the period to account for losses and delays.
- **Review cadence:** Weekly

#### 6. Client Concentration

- **Definition:** Revenue percentage from your top clients. High concentration means high risk.
- **Formula:** `(Revenue from top N clients / Total revenue) x 100`
- **Target guidance:** No single client should represent more than 25% of revenue. Top 3 clients should be below 50%. If you are above these thresholds, diversification is a strategic priority.
- **Review cadence:** Monthly

### Growth Metrics

#### 7. Backlog

- **Definition:** Contracted but not yet delivered revenue. Shows your future revenue visibility.
- **Formula:** `SUM(contracted revenue) - SUM(revenue recognized to date)`
- **Target guidance:** Healthy backlog covers 2-4 months of revenue at current run rate.
- **Review cadence:** Monthly

#### 8. Win Rate

- **Definition:** Percentage of proposals that convert to signed engagements.
- **Formula:** `(Proposals won / Total proposals submitted) x 100`
- **Target guidance:** 25-40% for competitive bids. 50-70% for referral and repeat work. Below 20% indicates a proposal quality or positioning problem.
- **Review cadence:** Monthly

#### 9. Average Engagement Size

- **Definition:** Average revenue per client engagement. Tracks whether you are moving toward larger, more strategic work.
- **Formula:** `Total revenue from engagements closed / Number of engagements closed`
- **Target guidance:** Should trend upward over time. If flat, evaluate packaging and pricing strategy.
- **Review cadence:** Quarterly

#### 10. Client Satisfaction Score (CSAT or NPS)

- **Definition:** Direct measurement of client satisfaction, typically gathered through surveys at engagement milestones or completion.
- **Formula:** NPS: `% Promoters (9-10) - % Detractors (0-6)` / CSAT: `(Positive responses / Total responses) x 100`
- **Target guidance:** NPS above 50 is strong for professional services. CSAT above 85% is solid.
- **Review cadence:** At engagement milestones (not less than quarterly)

#### 11. Employee Turnover Rate

- **Definition:** Staff retention. In professional services, your people are your product. Turnover directly impacts delivery quality, client relationships, and profitability.
- **Formula:** `(Number of departures during period / Average headcount during period) x 100`
- **Target guidance:** Annual turnover below 15% for consulting. Below 20% for agencies. Above these thresholds, investigate compensation, workload, and culture.
- **Review cadence:** Quarterly

#### 12. Revenue Growth Rate

- **Definition:** Period-over-period revenue growth.
- **Formula:** `((Current period revenue - Prior period revenue) / Prior period revenue) x 100`
- **Target guidance:** 15-25% annual growth is strong for established professional services firms. Higher for firms under $5M in revenue.
- **Review cadence:** Monthly (compare year-over-year to account for seasonality)

---

## Retail (Brick-and-Mortar and Omnichannel)

Retail KPIs focus on store productivity, inventory management, and customer value. Your dashboard should answer: "Are our stores productive, is our inventory healthy, and are we growing customer value?"

### Core Metrics

#### 1. Sales Per Square Foot

- **Definition:** The gold standard of retail productivity. Measures how effectively you are using your physical space.
- **Formula:** `Total net sales / Total selling square footage`
- **Target guidance:** Varies dramatically by category. Convenience stores: $400-$600/sq ft. Apparel: $200-$400/sq ft. Apple stores famously exceed $5,000/sq ft. Track against your own trend and category benchmarks.
- **Review cadence:** Monthly

#### 2. Same-Store Sales Growth (Comps)

- **Definition:** Revenue growth from stores that have been open for at least 12 months. Eliminates the effect of new store openings to show organic growth.
- **Formula:** `((This period revenue from comp stores - Same period prior year revenue from same stores) / Prior year revenue) x 100`
- **Target guidance:** Positive comps is the goal. 3-5% annual same-store growth is solid. Negative comps for more than two consecutive quarters is a red flag.
- **Review cadence:** Monthly

#### 3. Gross Margin Return on Investment (GMROI)

- **Definition:** Measures how much gross profit you earn for every dollar invested in inventory. Combines margin and turnover into one number.
- **Formula:** `Gross profit / Average inventory cost`
- **Target guidance:** Above 3.0 is strong. Below 2.0 indicates either margin or turnover issues. The best retailers optimize this by category.
- **Review cadence:** Monthly (by category)

#### 4. Conversion Rate (Foot Traffic to Sale)

- **Definition:** Percentage of store visitors who make a purchase. Requires traffic counting technology.
- **Formula:** `(Number of transactions / Number of store visitors) x 100`
- **Target guidance:** 20-40% for specialty retail. 15-25% for general merchandise. Track by day-of-week and hour to optimize staffing.
- **Review cadence:** Weekly

#### 5. Average Transaction Value (ATV)

- **Definition:** Average dollar amount per transaction. The in-store equivalent of AOV.
- **Formula:** `Total net sales / Number of transactions`
- **Target guidance:** Track trend over time. Use suggestive selling, merchandising, and bundling to increase.
- **Review cadence:** Weekly

#### 6. Inventory Shrinkage Rate

- **Definition:** The percentage of inventory lost to theft, damage, administrative error, or vendor fraud.
- **Formula:** `(Recorded inventory value - Actual inventory value) / Recorded inventory value x 100`
- **Target guidance:** Industry average is 1.4-1.6%. Below 1% is well-controlled. Above 2% requires immediate investigation.
- **Review cadence:** After each inventory count (quarterly at minimum)

### Growth Metrics

#### 7. Sell-Through Rate

- **Definition:** The percentage of inventory received that is sold within a given period. Critical for seasonal and perishable goods.
- **Formula:** `(Units sold / Units received) x 100`
- **Target guidance:** 80%+ within the selling season for seasonal goods. Track by SKU category to identify slow movers early.
- **Review cadence:** Weekly for seasonal items, monthly for evergreen

#### 8. Customer Retention Rate

- **Definition:** Percentage of customers who return to make another purchase within a defined period.
- **Formula:** `(Customers who purchased in both current and prior period / Customers who purchased in prior period) x 100`
- **Target guidance:** 30-40% annual retention for general retail. 50%+ for specialty retail with loyalty programs.
- **Review cadence:** Monthly

#### 9. Units Per Transaction (UPT)

- **Definition:** Average number of items per sale. Measures cross-selling effectiveness.
- **Formula:** `Total units sold / Total number of transactions`
- **Target guidance:** Track trend. Increasing UPT is a strong signal that merchandising and staff training are working.
- **Review cadence:** Weekly

#### 10. Labor Cost as Percentage of Revenue

- **Definition:** Staff costs relative to sales. The primary controllable expense in retail.
- **Formula:** `(Total labor cost including benefits / Total net sales) x 100`
- **Target guidance:** 10-15% for efficient retail operations. Higher for service-intensive formats. Optimize by aligning staff scheduling with traffic patterns.
- **Review cadence:** Weekly

#### 11. Stockout Rate

- **Definition:** Percentage of SKUs that are out of stock at any given time. Every stockout is a lost sale and a customer trust issue.
- **Formula:** `(Number of SKUs out of stock / Total active SKUs) x 100`
- **Target guidance:** Below 5% on core items. Below 2% on top sellers.
- **Review cadence:** Daily (automated alerts for top sellers)

#### 12. Sales Per Employee Hour

- **Definition:** Revenue generated per labor hour. Measures staff productivity.
- **Formula:** `Total net sales / Total employee hours worked`
- **Target guidance:** Varies by format. Track against your own trend and use to identify top-performing stores and staff.
- **Review cadence:** Weekly

---

## Food & Beverage (Restaurants, Cafes, Bars, Food Trucks)

Food and beverage businesses operate on thin margins with high variability. Your dashboard should answer: "Are we controlling food costs, are we filling seats, and are we making money on each check?"

### Core Metrics

#### 1. Food Cost Percentage

- **Definition:** The cost of ingredients as a percentage of food sales. This is the metric that makes or breaks restaurant profitability.
- **Formula:** `(Beginning inventory + Purchases - Ending inventory) / Food sales x 100`
- **Note:** Use actual food cost (inventory-based), not theoretical food cost (recipe-based). The gap between the two is your waste, theft, and portioning variance.
- **Target guidance:** 28-35% for full-service restaurants. 25-30% for fast casual. 20-25% for coffee shops (beverage-heavy). Above 35% requires immediate investigation into waste, portioning, or supplier pricing.
- **Review cadence:** Weekly

#### 2. Pour Cost (Beverage Cost Percentage)

- **Definition:** Cost of beverage ingredients as a percentage of beverage sales. Bars and beverage-heavy operations live and die here.
- **Formula:** `(Beginning bar inventory + Purchases - Ending bar inventory) / Beverage sales x 100`
- **Target guidance:** 18-24% for beer. 14-20% for liquor. 10-15% for wine by the glass. 20-25% blended. High pour cost usually indicates over-pouring, unrecorded comps, or theft.
- **Review cadence:** Weekly

#### 3. Labor Cost Percentage

- **Definition:** Total labor expense (wages, salaries, taxes, benefits) as a percentage of total revenue. The other major controllable cost.
- **Formula:** `(Total labor cost / Total revenue) x 100`
- **Target guidance:** 25-35% for full-service. 20-28% for fast casual. Combined food + labor (called "prime cost") should be below 65% of revenue. Above 65% prime cost means you are likely not profitable.
- **Review cadence:** Weekly

#### 4. Prime Cost

- **Definition:** The sum of food cost and labor cost. The most important profitability metric in food & beverage. If prime cost is out of control, nothing else can save you.
- **Formula:** `Total food cost + Total beverage cost + Total labor cost`
- **As percentage:** `Prime cost / Total revenue x 100`
- **Target guidance:** Below 60% of revenue is strong. 60-65% is acceptable. Above 65% requires immediate action.
- **Review cadence:** Weekly

#### 5. Average Check Size

- **Definition:** Average revenue per customer or per table. The revenue side of the profitability equation.
- **Formula:** `Total revenue / Number of covers (guests served)`
- **Alternative:** `Total revenue / Number of checks`
- **Target guidance:** Context-dependent. Track trend over time. Menu engineering, upselling training, and drink pairings are the standard levers.
- **Review cadence:** Daily

#### 6. Table Turnover Rate

- **Definition:** How many times each seat is occupied during a service period. In a fixed-capacity business, turnover is the revenue multiplier.
- **Formula:** `Number of covers served / Number of available seats`
- **Target guidance:** 1.5-2.5 turns per meal period for full-service. 3-5 for fast casual. Track by day-of-week and meal period.
- **Review cadence:** Daily

### Growth Metrics

#### 7. RevPASH (Revenue Per Available Seat Hour)

- **Definition:** The restaurant equivalent of RevPAR in hotels. Combines check size and turnover into a single capacity utilization metric.
- **Formula:** `Total revenue / (Available seats x Hours open)`
- **Target guidance:** Track trend over time and compare across meal periods (lunch vs. dinner) and days of week to identify optimization opportunities.
- **Review cadence:** Weekly

#### 8. Food Waste Percentage

- **Definition:** Tracks the gap between theoretical food cost (what recipes say you should spend) and actual food cost (what inventory says you did spend). This gap is waste, portioning errors, theft, or recording errors.
- **Formula:** `(Actual food cost - Theoretical food cost) / Theoretical food cost x 100`
- **Target guidance:** Below 5% variance is well-controlled. 5-10% is typical. Above 10% means you have a significant waste or control issue.
- **Review cadence:** Weekly

#### 9. Customer Count (Covers)

- **Definition:** Total number of guests served per period. The top of your revenue funnel.
- **Formula:** `Count of individual guests served`
- **Target guidance:** Track trend and compare year-over-year (food service is highly seasonal). Declining covers with stable check size means a traffic problem. Stable covers with declining check size means a spend problem.
- **Review cadence:** Daily

#### 10. Revenue Per Square Foot

- **Definition:** Similar to retail, measures how productively you are using your space.
- **Formula:** `Total revenue / Total square footage`
- **Target guidance:** Varies by format and market. Track against your own history and use when evaluating new locations.
- **Review cadence:** Monthly

#### 11. Online Order Percentage

- **Definition:** Share of total revenue from online ordering, delivery, and pickup. Important for understanding channel mix and planning staffing and production.
- **Formula:** `(Online order revenue / Total revenue) x 100`
- **Target guidance:** Varies by concept. Important to track because online orders often have different margin profiles (delivery fees vs. commission costs).
- **Review cadence:** Weekly

#### 12. Employee Turnover Rate

- **Definition:** Staff turnover rate. The restaurant industry averages 70-80% annual turnover. Reducing this even modestly saves significant training and recruitment costs.
- **Formula:** `(Number of separations during period / Average number of employees) x 100`
- **Target guidance:** Below 60% annual turnover is strong for restaurants. Below 40% for management positions. Each frontline departure costs an estimated $3,500-$5,000 in recruiting and training.
- **Review cadence:** Monthly

---

## Cross-Industry KPIs Worth Tracking

Regardless of your industry, consider adding these to your dashboard once your core metrics are stable:

| KPI | Formula | Why It Matters |
|-----|---------|----------------|
| **Cash Runway** | Cash on hand / Monthly burn rate | Tells you how many months you can operate at current spend. Every business should know this number. |
| **Accounts Receivable Aging** | Breakdown of outstanding invoices by 0-30, 31-60, 61-90, 90+ days | Revenue is not cash. Aging receivables indicate collection problems. |
| **Gross Profit Margin** | (Revenue - COGS) / Revenue x 100 | The foundation of your unit economics. |
| **Net Promoter Score (NPS)** | % Promoters - % Detractors | Leading indicator of growth through word of mouth. |
| **Employee Satisfaction (eNPS)** | Same as NPS but for employee sentiment | Leading indicator of turnover, which impacts everything else. |

---

## How to Set Targets

Do not guess at targets. Use this hierarchy:

1. **Your own historical data** — The best benchmark is your own performance last quarter or last year. Improve from there.
2. **Industry benchmarks** — Trade associations, industry reports, and peer groups publish benchmarks. Use them as sanity checks, not goals.
3. **First-principles math** — Work backward from your financial goals. If you need $1M in revenue and your AOV is $50, you need 20,000 orders. At a 3% conversion rate, you need ~667,000 sessions. Now you have a traffic target.
4. **Stretch targets** — Once you have a baseline, set a target that is 10-20% above current performance. Aggressive enough to drive change, realistic enough to be credible.

---

*Need help selecting and implementing KPIs for your specific business? Relay▸Launch builds custom measurement systems for small businesses. Reach out at [relaylaunch.com](https://relaylaunch.com).*
