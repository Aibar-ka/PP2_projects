import json

def print_interface_status(data):
    print("Interface Status")
    print("=" * 80)
    print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
    print("-" * 80)

    for interface in data['imdata']:
        dn = interface.get('DN', '')
        description = interface.get('Description', '')
        speed = interface.get('Speed', 'inherit')
        mtu = interface.get('MTU', '')
        print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))

with open('sample-data.json', 'r') as f:
    data = json.load(f)

print_interface_status(data)
