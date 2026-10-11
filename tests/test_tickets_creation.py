from campusflow.tickets import create_ticket

def test_ticket_creation():
    # when a good input is provided
    assert create_ticket(title="school", category="other", urgency="high", affected_users=15, status="Open", assigned_to="None") == None

    # testing invalid affected_users
    assert create_ticket(title="school", category="other", urgency="high", affected_users="lklk", status="Open", assigned_to="None") != None

    # testing for empty input fileds
    assert create_ticket(title="school", category="other", urgency="", affected_users="12", status="", assigned_to="None") != None



if __name__ == "__main__":
    unittest.main()