

def test_new_user(test_client, new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the username, password, and id fields are defined correctly
    """
    assert new_user.username == 'TestUser'
    assert new_user.password == 'password'
    assert isinstance(new_user.id, int)
