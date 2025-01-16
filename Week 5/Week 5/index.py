import sys

# Check if at least one name is passed (beyond the script name)
if len(sys.argv) > 1:
    # Print each name passed as an argument
    for arg in sys.argv[1:]:
        print(arg)
else:
    print("No names provided.")

