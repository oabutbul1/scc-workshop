# Copyright (c) 2026 Cisco Systems, Inc. and its affiliates
# SPDX-License-Identifier: Apache-2.0

"""
Organization Setup Workshop Template - Complete Organization Setup Flow

This workshop template demonstrates a complete workflow for setting up an organization
in Security Cloud Control. You will implement the API calls to complete each step.

PREREQUISITE STEPS - API Key Setup:

Step 1 – Log in to Security Cloud Control
    Go to Security Cloud Control URL: https://security.cisco.com/
    Login credential: will be provided

Step 2 – Copy Organization ID
    1. From left navigator, select "Platform Management"
    2. Select "Organization Details"
    3. Copy the Organization ID

Step 3 – Navigate to API Key
    1. From left navigator, select "Platform Management"
    2. Select "API Keys"

Step 4 – Create API Key
    1. Click "Generate API key"
    2. Fill in:
        a. Key name: <string> (example: apiKey-CiscoLive-Workshop)
        b. Description: <string>
        c. Key expiry: select Never expires
        d. Assign Roles select
            i.  Product: "Security Cloud Control"
            ii. Role: "Organization Administrator"

    ⚠️  IMPORTANT — Save Your Access token & refresh token.
    After creation, copy and store, this key will not be shown again.

Step 5 – Copy Claim Code
    Copy the claim code provided to you and paste it into the CLAIM_CODE variable in this template

Step 6 – Open VS Code and Install SDK
    1. Open VS Code
    2. Open the terminal in VS Code
    3. Install the Security Cloud Control SDK by running:
       pip install -e .

WORKSHOP EXERCISES:

You will implement the following workflow steps:
1. Getting organization details
2. Claiming subscriptions (Secure Access)
3. Inviting users
4. Creating admin groups
5. Adding users to groups

INSTRUCTIONS:
- Search for "TODO:" comments to find where you need to add code
- Simply delete the TODO comment lines to reveal the working code
- Reference the API Reference section in README.md for complete method documentation
- Estimated completion time: 30 minutes
"""

from scc_sdk import Client, SCCError

# ============================================================================
# CONFIGURATION - Update these values for your environment
# ============================================================================

# Security Cloud Control credentials
ACCESS_TOKEN = ""  # Replace with your access token

# Organization ID
ORG_ID = ""  # Replace with your organization IDKey

# Claim code for subscription
CLAIM_CODE = ""  # Replace with your claim code

# Users to invite (list of user details with email, first name, and last name)
USERS_TO_INVITE = [
    {"email": "member1@cl-workshop.com", "first_name": "Member1", "last_name": "Ciscolive"},
    {"email": "member2@cl-workshop.com", "first_name": "Member2", "last_name": "Ciscolive"},
    {"email": "member3@cl-workshop.com", "first_name": "Member3", "last_name": "Ciscolive"},
    {"email": "admin-org1@cl-workshop.com", "first_name": "Admin1", "last_name": "Org"},
    {"email": "admin-org2@cl-workshop.com", "first_name": "Admin2", "last_name": "Org"}
]




def get_organization_details(client):
    """Fetch and display organization details.
    
    EXERCISE 1: Implement this function to retrieve organization details.
    """
    print("=" * 80)
    print(f"\nSTEP 1: Get Org Details for: {ORG_ID}")
    print("=" * 80)

    # TODO: Use the client to get organization details
    # org = client.organizations.get(org_id=ORG_ID)
    
    # TODO: Print the organization details
    # client.organizations.print_details(org)
    
    return org

def claim_subscriptions(client):
    """Claim subscription.
    
    EXERCISE 2: Implement this function to read claim code details and create a subscription.
    """
    print("=" * 80)
    print("\nSTEP 2: Subscription Management - Claiming Subscription")
    print("\nSTEP 2.1: Checking existing subscriptions...")
    print("=" * 80)
    
    # TODO: List existing subscriptions for the organization
    # subs_list = client.subscriptions.list(org_id=ORG_ID)
    
    # TODO: Print the count of existing subscriptions
    print(f"  Found {len(subs_list)} existing subscription(s)")
        
    print("\nSTEP 2.2: Reading claim code details...")
    print("=" * 80)
    print(f"  Claim Code: {CLAIM_CODE}")
    
    try:
        # TODO: Read the claim code details
        # claim_info = client.subscriptions.read_claim_code(org_id=ORG_ID, claim_code=CLAIM_CODE)
        
        # TODO: Print the claim information
        # client.subscriptions.print_claim_info(claim_info)
        
        # Claim the subscription with the claim info
        # claim_single_subscription(client, CLAIM_CODE, "Subscription", claim_info)
    except SCCError as e:
        print(f"  ✗ Failed to read claim code: {e}")
        print("  Skipping subscription claim due to error reading claim code.")


def claim_single_subscription(client, claim_code, name, claim_info):
    """Claim a single subscription and handle errors.
    
    EXERCISE 2.1: Implement the subscription creation logic.
    """
    print(f"\nSTEP 2.3: Claiming {name} subscription...")
    print(f"  Claim Code: {claim_code}")
    
    # TODO: Build products list from claim_info using helper method
    # products = client.subscriptions.build_products_from_claim_info(claim_info)
    
    # Print selected products and regions
    for i, product in enumerate(products):
        product_info = claim_info.get("products", [])[i]
        print(f"  - Product: {product_info.get('name')}")
        print(f"    Region: {product.get('regionDescription')} ({product.get('regionCode')})") 
    
    # Create subscription using the claim code and products
    try:
        # TODO: Create the subscription
        #result = client.subscriptions.create(org_id=ORG_ID, claim_code=CLAIM_CODE, products=products)
        
        print(f"✓ {name} subscription claimed successfully")
        if result:
            print(f"  - Response: {result}")
        return result
    except SCCError as e:
        print(f"✗ Failed to claim {name} subscription: {e}")
        return None


def invite_users(client):
    """Invite users to the organization.
    
    EXERCISE 3: Implement the user invitation logic.
    """
    print("=" * 70)
    print("\nSTEP 3: User Management - Inviting Users")
    
    print(f"\nInviting {len(USERS_TO_INVITE)} users to the organization...")
    
    # Invite each user
    invited_count = 0
    for user_info in USERS_TO_INVITE:
        try:
            # TODO: Invite the user using the client
            # result = client.users.invite(
            #     org_id=ORG_ID,
            #    email=user_info['email'],
            #     first_name=user_info['first_name'],
            #     last_name=user_info['last_name']
            # )
            
            print(f"  ✓ {user_info['first_name']} {user_info['last_name']} ({user_info['email']})")
            invited_count += 1
        except SCCError as e:
            print(f"  ✗ {user_info['email']}: {e}")
    
    print(f"\n✓ Successfully invited {invited_count}/{len(USERS_TO_INVITE)} users")
    
    print("\nListing current users in organization:")
    
    # Check SCC UI to see invited users status
    # TODO: List all users in the organization
    # users_result = client.users.list(org_id=ORG_ID)
    
    # TODO: Get the users array from the result
    # current_users = users_result.get("users", [])
    
    # TODO: Print the count of total users
    print(f"  Found {len(current_users)} total users")


def create_admin_group(client, name="Products Admin Group", description="Administrative group for managing Cisco security products"):
    """Create an admin group with the specified name and description.
    
    EXERCISE 4: Implement the admin group creation logic.
    """
    print("=" * 70)
    print(f"\nSTEP 4: Admin Groups - Creating {name}")
    
    print(f"\nCreating '{name}'...")
    
    try:
        # TODO: Create the admin group
      #  products_admin_group = client.groups.create(
      #       org_id= ORG_ID,
      #       name=name,
      #       description=description
      #   )
        
        # TODO: Get the group ID from the response
        group_id = products_admin_group.get("id")
        
        print(f"✓ {name} created successfully")
        
        # TODO: Print the group details
      #  client.groups.print_details(products_admin_group)
        
        # TODO: Return the group_id
        return group_id
        
    except SCCError as e:
        print(f"✗ Failed to create {name}: {e}")
        print(f"\nAttempting to find existing {name}...")
        
        # TODO: List all groups to find if the group already exists
        groups_result = client.groups.list(org_id=ORG_ID)
        
        # TODO: Get the groups array
        groups = groups_result.get("groups", [])
        
        for group in groups:
            if group.get("name") == name:
                group_id = group.get("id")
                print(f"✓ Found existing {name}")
                client.groups.print_details(group)
                return group_id
        
        print(f"✗ Could not create or find {name}")
        return None


def add_users_to_group(client, group_id, user_emails):
    """Add users to an admin group.
    
    EXERCISE 4.1: Implement the logic to add users to a group.
    
    Args:
        client: SCC client instance
        group_id: The group ID to add users to
        user_emails: List of user email addresses to add
    """
    print("=" * 70)
    print(f"\nSTEP 4.1: Adding Users to Admin Group")
    print(f"  Group ID: {group_id}")
    
    print(f"\nAdding {len(user_emails)} user(s) to the group...")
    
    # Prepare user operations for patch
    user_operations = [{"operation": "add", "id": email} for email in user_emails]
    
    try:
        # TODO: Patch the group to add users
     #   result = client.groups.patch(
     #        org_id=ORG_ID,
     #        group_id=group_id,
     #        users=user_operations
     #    )
        
        print(f"✓ Successfully added users to group")
        for email in user_emails:
            print(f"  - {email}")
        
        return result
    except SCCError as e:
        print(f"✗ Failed to add users to group: {e}")
        return None





def print_summary(org, group_id):
    """Print the setup summary."""
    print("=" * 70)
    print("\nSETUP COMPLETE - Summary")
    
    print("\n✓ Organization Details Retrieved:")
    print(f"  - {org.get('name')} ({ORG_ID})")
    
    print("\n✓ Subscription Claimed:")
    print("  - Subscription")
    
    print("\n✓ Users Management:")
    print(f"  - {len(USERS_TO_INVITE)} users invited")
    
    print("\n✓ Admin Group Created:")
    print(f"  - Products Admin Group (ID: {group_id})")
    print(f"  - Admin users added to group")
    
    print("\nOrganization Setup Successfully Completed!")


def main():
    """Execute the organization setup workflow."""
    print('Initializing SCC SDK Client...')
    
    # TODO: Initialize the client with the ACCESS_TOKEN
    client = Client(access_token=ACCESS_TOKEN, debug=True)
    
    try:
        print("=" * 80)
        print("Organization Setup - Security Cloud Control")
        
        # EXERCISE 1: Get organization details
        org = get_organization_details(client)
        
        # EXERCISE 2: Claim subscriptions
        claim_subscriptions(client)
        
        # EXERCISE 3: Invite users
        invite_users(client)
        
        # EXERCISE 4: Create admin group
        group_id = create_admin_group(client)
        
        if not group_id:
            print("\n✗ Failed to create or find admin group. Exiting...")
            return
        
        # EXERCISE 4.1: Add admin users to the group
        admin_users = ["admin-org1@cl-workshop.com", "admin-org2@cl-workshop.com"]
        add_users_to_group(client, group_id, admin_users)
        
        print_summary(org, group_id)
        
    except SCCError as e:
        print(f"\n✗ Error occurred: {e}")
        print(f"   Status Code: {e.status_code}")
        print(f"   Response: {e.response}")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")


if __name__ == "__main__":
    main()
