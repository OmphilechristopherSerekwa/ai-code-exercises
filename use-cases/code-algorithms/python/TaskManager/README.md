# Task Management System

## Usage Instructions
### Prerequisites
- Python 3.11 or higher
- No additional external dependencies required

### Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd task-manager
```

2. No additional installation steps are required, since the project uses only Python standard library modules.

### Run the CLI

The CLI provides various commands to manage tasks:

1. Create a new task:
```bash
python cli.py create "Task Title" --description "Task description" --priority 2 --due "2024-01-31" --tags "tag1,tag2"
```

2. List tasks:
```bash
# List all tasks
python cli.py list

# List by status (todo, in_progress, review, done)
python cli.py list --status todo

# List by priority (1=LOW, 2=MEDIUM, 3=HIGH, 4=URGENT)
python cli.py list --priority 3

# List overdue tasks
python cli.py list --overdue
```

3. Update tasks:
```bash
# Update task status
python cli.py status <task_id> <new_status>

# Update task priority
python cli.py priority <task_id> <new_priority>

# Update task due date
python cli.py due <task_id> "2024-02-15"
```

4. Manage tags:
```bash
# Add a tag
python cli.py tag <task_id> "new-tag"

# Remove a tag
python cli.py untag <task_id> "tag-to-remove"
```

5. Export tasks to CSV:
```bash
# Export all tasks to a CSV file
python cli.py export tasks.csv

# Export only overdue tasks
python cli.py export overdue_tasks.csv --overdue

# Export tasks filtered by status or priority
python cli.py export todo_tasks.csv --status todo
python cli.py export urgent_tasks.csv --priority 4
```

6. View task details and statistics:
```bash
# Show task details
python cli.py show <task_id>

# Show task statistics
python cli.py stats
```

### Run the Tests
Run the unit tests using Python's unittest framework:

```bash
# Run tests with basic output
python -m unittest discover tests

# Run tests with verbose output
python -m unittest discover -v tests
```
