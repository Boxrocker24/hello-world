# hello-world
I am learning how to use git!

Case Study: Engineering a Root-Cause Diagnostic Matrix to Eliminate SLA Breaches in Teleradiology
The Business Problem

A leading national teleradiology provider was experiencing chronic Turnaround Time (TAT) breaches during evening and weekend shifts. The prevailing operational assumption was that these Service Level Agreement (SLA) failures were caused by "bursty," unpredictable hospital emergency room volume overwhelming the scheduled staff. Because the company lacked hard contractual penalties for late reads, the operational urgency was low, masking a massive, unquantified financial threat: Invisible Client Churn Risk.
My Role & The Infrastructure

Before I could diagnose the problem, I had to build the foundational data architecture to make the analysis possible.

    Data Engineering: I engineered and maintained the automated data pipelines, routing raw HL7 hospital arrival data and timestamped operational logs into Google BigQuery.

    Scheduling Integration: I integrated the company’s complex scheduling platform into Supabase, allowing us to query exact shift blocks against row-level production data.

    Full-Stack Analytics: With the pipelines established, I led the end-to-end operational analysis to bridge the gap between abstract data and human behavior.

The Investigation & Key Methodologies
1. Debunking the "Unpredictable Volume" Myth

Using BigQuery, I mapped the arrival curve of high-priority (STAT) RVUs across an 8-week period. The data revealed that demand was not unpredictable; it was a flat, highly consistent curve. The breaches were not a demand problem—they were a capacity problem. The scheduled core team was vastly undersized for the baseline volume, making the company entirely dependent on an unscheduled, variable "per-case" workforce to clear the queue.
2. Eliminating Volume Bias: The "Garbage Collection Ratio" (GCR)

To determine exactly when the queue was collapsing, I needed to separate healthy shifts from failing shifts. However, looking at raw clearance volume created "Volume Bias"—busy hours looked terrible simply because the numbers were larger.

To solve this, I engineered a normalized metric called the Garbage Collection Ratio (GCR).

    I tracked the "Age of Clearance" for every RVU (cleared in the same hour, 1 hour ago, or 2+ hours ago).

    GCR = (RVUs Cleared from 2+ Hours Ago / Total RVUs Cleared) * 100.

    If a shift had a GCR > 30%, they had lost control of the queue and were strictly doing "garbage collection" on rotting cases, regardless of their total output.

3. The Root Cause Diagnostic Matrix

Identifying when the queue collapsed wasn't enough; I needed to prove why. I built a Python-based diagnostic engine that overlaid the Garbage Collection Ratio (Symptom) with the Volatility Score / Coefficient of Variation (Cause) and Net Hourly Velocity (Real-time bleeding).

This matrix scientifically categorized every hour of the week:

    High Volatility + High GCR: True "Bursty Arrivals" (Hospital's fault).

    Low Volatility + High GCR: "Inherited Backlog" (Prior shift's fault).

The Breakthrough: The matrix proved that 80% of queue collapses were "Inherited Backlog." The evening shifts were failing not because of unpredictable volume, but because the variable workforce predictably logged off during the 5:00 PM – 8:00 PM "Dinner Desert." When the late-night doctors logged on at 9:00 PM, they spent 57% of their shift doing garbage collection for the prior shift's abandonment.
4. Humanizing the Data: Roster Attrition

To make the data actionable for the executive team, I wrote a custom parsing script to extract the exact physical rosters of who was logged on during every hour. This provided irrefutable proof of roster attrition: we were losing an average of 28% of our active workforce precisely when the queue began to bleed (Negative Net Velocity).
The Strategic Outcome & Business Impact

Instead of guessing at scheduling fixes, I provided the executive team with a surgical, hour-by-hour operational playbook:

    Shifted from Hiring to Retention: Proved that hiring more doctors for the hours where SLAs breached (e.g., 9:00 PM) was a waste of margin. The optimal strategy was to fix the preceding shifts (5:00 PM) to prevent the fire from starting.

    Dynamic Surge Pricing Strategy: Identified the exact 8 hours a week where volume was genuinely volatile. Recommended deploying a targeted, automated Surge Pricing model (+$/RVU) strictly during these specific hours, shifting the company from static scheduling to highly efficient variable capacity.

    Revenue Protection: By framing chronic TAT breaches as an "Invisible Churn Penalty" that erodes pricing power at contract renewal, I successfully aligned the operations and finance teams to invest in targeted surge pay, protecting millions in annual recurring revenue.