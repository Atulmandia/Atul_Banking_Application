from pprint import pprint

#backToProfile function creates a back option, which when called takes the user to login options.
def backToProfile(username):
    op=int(input("\nEnter 1 to go back = "))
    if op==1:
        import Options
        Options.ProfileOptions(username)
    else :
        pprint("Wrong Option Selected")
        backToProfile(username)