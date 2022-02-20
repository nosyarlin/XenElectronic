from models.user import User


def test_new_user(test_client):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the username, password, and id fields are defined correctly
    """
    user = User.find_by_username('TestUser')
    assert user.username == 'TestUser'
    assert user.password == 'password'
    assert isinstance(user.id, int)
