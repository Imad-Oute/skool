# Step 6: Finalization & Audit Tracking

**Objective:** Finalize the content unit, save to proper location, and prepare for audit tracking.

## Instructions

Execute the following in sequence:

### 1. Final Review

Present the complete content unit to the user:

```
=== CONTENT UNIT COMPLETE ===

Platform: {platform}
Topic: {topic} ({topicCategory})
Retention Mechanic: {retentionMechanic}
Core Reward: {coreReward}

[Display the formatted content from Step 5]

================================
```

Ask: "Is this content unit ready for publication, or do any sections need revision?"

### 2. Handle Revisions

**If revisions needed:**

- Ask: "Which section needs revision?" (Topic, Structure, Content)
- Return to appropriate step file
- After revision, return here

**If approved:**

- Proceed to section 3

### 3. Generate Filename & Save

Create a filename based on the topic:

- Format: `YYYY-MM-DD-{topic-slug}.md`
- Example: `2026-04-06-topic-matrix-guide.md`

Save the complete output file to:
`{project-root}/output/content/{filename}`

Update frontmatter:

```yaml
stepsCompleted: [1, 2, 3, 4, 5, 6]
status: complete
filename: { generated filename }
completedDate: { current date }
```

### 4. Audit Tracking Instructions

Display to the user:

```
✓ Content Unit Complete!

NEXT STEPS FOR TRACKING:

1. **Manual Submission:**
   - Copy the content to your publishing platform
   - Record the publication URL

2. **Audit Log Entry:**
   - File: {project-root}/logs/content-performance.csv
   - Add row: Date, Platform, Topic, URL, Initial Engagement (to be filled)

3. **Performance Tracking:**
   - Day 7: Check engagement metrics
   - Day 30: Evaluate against benchmarks
   - Update audit log with results

4. **Feedback Loop:**
   - Did Hook perform? (CTR / Stop rate)
   - Did Retention hold? (AVD / Read depth)
   - Did Reward land? (Shares / Comments / Conversions)
   - Use insights to refine next content unit
```

### 5. Systematic Iteration Notes

Append to output file:

```markdown
## Post-Publication Checklist

**Immediate (Day 0):**

- [ ] Content published to {platform}
- [ ] URL recorded in audit log
- [ ] Initial distribution completed

**Day 7 Review:**

- [ ] Engagement metrics recorded
- [ ] Hook performance assessed (did it stop the scroll?)
- [ ] Retention performance assessed (did they consume fully?)

**Day 30 Review:**

- [ ] Reward performance assessed (shares, comments, actions)
- [ ] Lessons learned documented
- [ ] Adjustments noted for next content unit

---

## Workflow Complete

This content unit is ready for the Content Assembly Line.

**Asset Philosophy Reminder:**
Content is the tool; Audience is the asset. Monitor not just engagement, but audience health (growth, retention, sentiment).
```

### 6. Final Output

Show the user:

```
===================================
CONTENT ARCHITECT: WORKFLOW COMPLETE
===================================

Output File: {project-root}/output/content/{filename}

The content unit has been architected using:
✓ 5-Category Topic Matrix
✓ Retention Mechanics
✓ Value Density Validation
✓ Platform Optimization

Follow the post-publication checklist for tracking and iteration.

The Content Assembly Line is operational.
```

---

**END OF STEP 6**
**END OF WORKFLOW**
