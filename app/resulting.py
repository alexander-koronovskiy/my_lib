def handle_df(df):

    # validation
    if df["profile"].empty() or df["dfa_transform"].empty():
        raise KeyError("You transmit incomplete dataframe")

    # save df to file
    df.to_csv("output.csv", index=False)  # header=none

    # saving images
