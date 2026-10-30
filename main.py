
import os
from dotenv import load_dotenv

load_dotenv()

name = os.getenv("STUDENT_NAME")
college = os.getenv("COLLEGE")
goal = os.getenv("GOAL")

print("Name:", name)
print("College:", college)
print("Goal:", goal)
