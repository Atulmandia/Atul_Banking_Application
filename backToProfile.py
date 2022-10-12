def backToProfile(username):

    """
        this function creates a back option, which when called takes the user to login options.
        :param username: the username entered
    """

    op=int(input("\nEnter 1 to go back = "))
    if op==1:
        import Options
        Options.ProfileOptions(username)
    else :
        print("Wrong Option Selected")
        backToProfile(username)