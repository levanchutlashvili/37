from jar import Jar

def test_init():
    # Test initialization with default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar._cookies == 0

    # Test initialization with custom capacity
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar._cookies == 0

    # Test initialization with invalid capacity
    try:
        jar = Jar(-1)
    except ValueError:
        pass  # Expected behavior
    else:
        assert False, "Expected ValueError for negative capacity"

    try:
        jar = Jar(2.5)
    except ValueError:
        pass  # Expected behavior
    else:
        assert False, "Expected ValueError for non-integer capacity"

def test_str():
    # Test string representation with no cookies
    jar = Jar()
    assert str(jar) == ""

    # Test string representation with some cookies
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    assert jar._cookies == 3

    # Test string representation with maximum cookies
    jar.deposit(9)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    assert jar._cookies == 12

    # Test string representation with more cookies than capacity
    try:
        jar.deposit(1)
    except ValueError:
        pass  # Expected behavior
    else:
        assert False, "Expected ValueError for depositing more cookies than capacity"

def test_deposit():
    # Test depositing zero cookies
    jar = Jar()
    jar.deposit(0)
    assert jar._cookies == 0

    # Test depositing some cookies
    jar = Jar()
    jar.deposit(3)
    assert jar._cookies == 3

    # Test depositing too many cookies
    jar = Jar()
    try:
        jar.deposit(13)
    except ValueError:
        pass  # Expected behavior
    else:
        assert False, "Expected ValueError for depositing too many cookies"

    # Test depositing negative number of cookies
    jar = Jar()
    try:
        jar.deposit(-1)
    except ValueError:
        pass  # Expected behavior
    else:
        assert False, "Expected ValueError for depositing negative cookies"

    # Test depositing non-integer number of cookies
    jar = Jar()
    try:
        jar.deposit(2.5)
    except ValueError:
        pass  # Expected behavior
    else:
        assert False, "Expected ValueError for depositing non-integer cookies"