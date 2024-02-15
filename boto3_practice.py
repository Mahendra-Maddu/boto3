import boto3

def delete_unattached_snapshots():
    ec2_client = boto3.client('ec2')

    # Get a list of all snapshots
    response = ec2_client.describe_snapshots(OwnerIds=['self'])
    snapshots = response['Snapshots']
    

    # Filter out snapshots that are not attached to any volumes
    unattached_snapshots = [snapshot for snapshot in snapshots if 'VolumeId' not in snapshot]

    if not unattached_snapshots:
        print("No unattached snapshots found.")
        return

    # Delete unattached snapshots
    for snapshot in unattached_snapshots:
        snapshot_id = snapshot['SnapshotId']
        print(f"Deleting unattached snapshot: {snapshot_id}")
        ec2_client.delete_snapshot(SnapshotId=snapshot_id)

    print("Unattached snapshots deleted successfully.")

if __name__ == "__main__":
    delete_unattached_snapshots()
