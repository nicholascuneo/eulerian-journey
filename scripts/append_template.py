from pathlib import Path

def append_template(problem_file, template_file):
    """
    Appends content of template_file to problem_file

    Params:
    problem_file generated by EulerPy
    template_file containing solution template
    """
    
    # Ensure both files exist
    problem_path = Path(problem_file)
    template_path = Path(template_file)

    # If either file does not exist, print error message and exit script
    if not problem_path.exists():
        print(f"Error: Ensure {problem_file} exists.")
        return
    elif not template_path.exists():
        print(f"Error: Ensure {template_file} exists.")
        return
    
    # Read content of both files
    problem_content = problem_path.read_text().strip()
    template_content = template_path.read_text().strip()

    # Combine contents
    combined_content = f"{problem_content}\n\n{template_content}"

    # Write back to problem file
    problem_path.write_text(combined_content)
    print(f"Template successfully appended to {problem_file}")

if __name__ == "__main__":
    import sys

    # Check if script is run with correct number of arguments
    if len(sys.argv) != 3:
        # Print usage message if arguments are missing
        print("Usage: python append_template.py <problem_file> <template_file>")
    else:
        # Extract arguments
        problem = sys.argv[1]
        template = sys.argv[2]

        # Call function with provided arguments
        append_template(problem, template)


