def employee_info(emp_id, name, role="Developer", *skills, **details):
    print("=== Employee Info ===")
    
    # Positional arguments
    print(f"ID: {emp_id}")
    print(f"Name: {name}")
    
    # Default argument
    print(f"Role: {role}")
    
    # *args (variable positional arguments)
    print("\nSkills:")
    if skills:
        for skill in skills:
            print(f"- {skill}")
    else:
        print("No skills provided")
    
    # **kwargs (variable keyword arguments)
    print("\nAdditional Details:")
    if details:
        for key, value in details.items():
            print(f"{key}: {value}")
    else:
        print("No additional details")
    
    print("=====================\n")


# 🔥 Function Calls (Different Scenarios)

# 1. Only positional arguments
employee_info(101, "Satish")

# 2. Positional + default override
employee_info(102, "Kumar", "Senior Engineer")

# 3. With *args (skills)
employee_info(103, "Rahul", "Backend Dev", "Python", "Django", "Rails")

# 4. With **kwargs (extra details)
employee_info(104, "Anita", location="Bangalore", experience="5 years")

# 5. All combined
employee_info(
    105,
    "Priya",
    "Full Stack Dev",
    "React",
    "Node.js",
    "AWS",
    location="Hyderabad",
    experience="6 years",
    salary="15 LPA"
)

# python3 Basics/funcs/argument_types.py