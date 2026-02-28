Here is a revised version of the case study. It is stripped of all exact internal numbers, explicitly mentions data obfuscation for confidentiality, and is completely reframed to speak the language of a CEO or Business Owner.

It focuses heavily on the *journey*—how a simple weekend investigation evolved into a company-wide operational overhaul.

---

# Case Study: Turning a Weekend Crisis into a Systemic Operational Strategy

*(Note: Specific company metrics, hours, and financial figures have been generalized or obfuscated to comply with confidentiality requirements.)*

## The Catalyst: A Single Bad Weekend

It started with a standard operational headache: our teleradiology practice experienced severe Turnaround Time (TAT) Service Level Agreement (SLA) breaches over a single weekend. The prevailing assumption from the operations team was that the hospital Emergency Rooms had simply dropped an unpredictable "bomb" of volume on our doctors.

I was tasked with diagnosing what went wrong. To do this, I engineered a data pipeline linking our raw HL7 hospital arrival data (in Google BigQuery) with our complex physician scheduling platform (in Supabase).

When I analyzed that single weekend, I found a discrepancy: the hospital volume didn't actually spike. The volume was normal, but our processing capacity had silently evaporated.

## Scaling the Scope: The CEO Pitch

I realized this wasn't an anomaly. I expanded the data pipeline to pull months of historical shift data. The pattern was undeniable: we weren't experiencing unpredictable volume spikes; we were experiencing a highly predictable, systemic capacity drop-off during specific evening and weekend hours. The core scheduled team was too small, leaving the company entirely dependent on a variable, unscheduled "per-case" workforce that predictably logged off at the exact same times every week.

I took these initial findings to the CEO. I reframed the problem from a "customer service complaint" to a massive financial threat: **Invisible Client Churn**. By routinely breaching SLAs, we were eroding our pricing power for future contract renewals. Recognizing the financial risk, the CEO gave me the green light to dive deeper and find the exact root cause of the bleeding.

## The Gold Mine: Engineering the Diagnostic Matrix

With executive buy-in, I moved beyond standard operational reporting and built a custom algorithmic model to find exactly *where* the queue was breaking. Standard metrics like "total cases read" were dangerously misleading—they made busy shifts look highly productive, even if the queue was collapsing.

To cut through the noise, I engineered two proprietary business metrics:

1. **The Garbage Collection Ratio (GCR):** Instead of looking at raw volume, I tracked the "age" of the cases being read. If a high percentage of a shift’s work consisted of cases that were already hours old, that shift wasn't productive—they were just doing "garbage collection."
2. **The Volatility Score (CV):** I measured the week-over-week predictability of the incoming hospital volume to determine if the environment was chaotic or stable.

When I intersected these metrics, it created an absolute gold mine of operational truth.

## Revealing the Exact Bleed

The Diagnostic Matrix completely upended the company’s assumptions. We assumed our late-night teams were failing because they were too slow. The matrix proved they were actually innocent.

Over **80% of our SLA queue collapses were caused by "Inherited Backlog."** The late-night volume was perfectly predictable, but when those doctors logged on, they spent the majority of their shift shoveling out rotting backlog left behind by the early-evening shift.

To make this actionable, I added a **Net Velocity** metric (tracking real-time queue expansion) and mapped the physical roster of doctors logged in hour-by-hour. I was able to show the executive team the exact minute the bleeding started:

* We could watch the roster naturally shrink as doctors logged off for dinner.
* We could watch the Net Velocity instantly turn negative (meaning the backlog was actively growing).
* We could watch the subsequent shift log on hours later and get completely buried by the rotting queue, causing the SLAs to formally breach.

## The Business Impact & Actionable Strategy

By tracking the exact life cycle of an SLA breach, I prevented the company from making a massive resource allocation mistake.

If we had just looked at the surface-level SLA breaches, the company would have spent significant capital hiring full-time doctors for the late-night shifts. My analysis proved that adding doctors to the late-night shift would be treating the symptom, not the disease.

Instead, I delivered a surgical, cost-efficient strategy:

* **Targeted Shift Retention:** We adjusted the scheduling focus to the hours *preceding* the collapses, preventing the fire from ever starting.
* **Automated Surge Pricing:** For the minority of hours where hospital volume was genuinely volatile and unpredictable, I recommended a dynamic "Surge Pricing" model. This shifted our labor strategy to a variable cost that only triggered when revenue (volume) actively supported it.

**The Result:** What began as a request to review a single weekend of bad metrics evolved into a complete overhaul of the company’s capacity strategy—aligning data engineering, operational reality, and executive financial goals to protect millions in recurring revenue.