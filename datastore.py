import argparse
from google.cloud import datastore

def update_entity(project_id, entity_id, category, done, priority, description):
    client = datastore.Client(project=project_id)

    entity_key = client.key("Task", entity_id)

    task = datastore.Entity(key=entity_key)

    task.update(
        {
            "category": category,
            "done": done,
            "priority": priority,
            "description": description,
        }
    )

    client.put(task)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update Entity in Datastore")
    parser.add_argument("project", help="Google Cloud project ID")
    parser.add_argument("entity_id", help="ID of the entity to update")
    parser.add_argument("category", help="New category of the entity")
    parser.add_argument("done", type=bool, help="New completion status (True or False)")
    parser.add_argument("priority", type=int, help="New priority of the entity")
    parser.add_argument("description", help="New description of the entity")
    args = parser.parse_args()

    update_entity(
        args.project,
        args.entity_id,
        args.category,
        args.done,
        args.priority,
        args.description,
    )
