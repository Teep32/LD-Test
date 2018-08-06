import ldclient

if __name__ == "__main__":
    ldclient.set_sdk_key("sdk-48a8550a-99ed-4633-81de-9ae1655799ca")

user = {
    "key": "bob@example.com",
    "firstName":"Bob",
    "lastName":"Loblaw",
    "custom": {
        "groups":"beta_testers"
    }
}

show_feature = ldclient.get().variation("pge-model-a", user, False)

if show_feature:
    print("Showing your feature")
else:
    print("Not showing your feature")


show_feature2 = ldclient.get().variation("pge-model-b", user, False)

if show_feature2:
    print("Showing your 2nd feature")
else:
    print("Not showing your 2nd feature")


show_feature3 = ldclient.get().variation("pge-multivar", user, 'maybe')
if show_feature3 == 'yes':
    {
        print("YES!!!")
    }
if show_feature3 == 'no':
    {
        print("NOOOOOOOOOOOPE!")
    }
if show_feature3 == 'maybe':
    {
        print("I have no fucking clue")
    }


ldclient.get().close()
