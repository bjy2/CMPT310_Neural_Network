import subprocess

def run_autograder_question_q3(n):
    for i in range(n):
        print(f"\n\n========== Run #{i + 1} (Question q5) ==========\n")
        try:
            result = subprocess.run(
                ["python3", "autograder.py", "-q", "q5"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            print(result.stdout)
        except Exception as e:
            print(f"Error during run #{i + 1}: {e}")

# Run the autograder on question q3 ten times
run_autograder_question_q3(10)
