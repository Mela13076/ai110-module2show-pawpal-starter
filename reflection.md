# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Three core actions user should be able to perform: 
    1. Add and manage pet tasks
    2. View daily care schedule
    3. Update pet information
    4. add a pet

- Briefly describe your initial UML design:
    -The inital UML deisgn classes for Owner, Pet, Scheduler, and task. IT will focus on separating data, task managemetn, and scheduling. 
- What classes did you include, and what responsibilities did you assign to each?
    - Owner: includes the pet's owner information like name and availability. 
    - Pet: includes pet information like name, type, breed, and any special care instructions.
    - Task: Each task will have the name, duration, priority, and category. 
    - Scheduler: This will handle generating the daily care plan. It will concider task priority, time constriants, and create a final schedule. 
    - Task Manager: This will handle adding, remvoing, and updating tasks. 

**b. Design changes**

- Did your design change during implementation? If yes, describe at least one change and why you made it.
    - Yes, I decided not to create task manager and instead have the task as a list associated with the pet. 


---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

    - My detect_conflicts method by iterating over adjacent tasks using zip() instead of index-based loops, which improves readability and reduces indexing logic. Performance remains optimal at O(n log n) due to sorting, and no additional optimization is needed.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
