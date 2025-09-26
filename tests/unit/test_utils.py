import utils


def test_hash_password():
    test_password = "test"
    test_salt = "000"
    # hash(password="test", salt="000")
    known_hash = "6dba17b3305f3199d453789aae0bac4011839996e115cdb49d2bfbc18f419e79"
    hashed_password = utils.hash_password(test_password, test_salt)
    assert hashed_password == known_hash


def test_is_valid_email():
    good_email = "foo@bar.com"
    assert utils.is_valid_email(good_email)

    bad_email = "not-an-email"
    assert not utils.is_valid_email(bad_email)
