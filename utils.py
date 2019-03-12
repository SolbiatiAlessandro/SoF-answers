"""module with utils function for answering SOF questions"""
"""
import pandas as pd
df = pd.DataFrame(['Copy me to clipboard'])
df.to_clipboard(index=False,header=False)
"""


def SOF_to_df(df_input):
    """
    Args:
        df_input (string): output of print(pd.DataFrame)
    Return:
        df (pd.DataFrame)
    """
    import pandas as pd

    raw = [s.split(' ') for s in df_input.split('\n')]
    cleaned = []
    for section in raw:
        if section != ['']:
            cleaned.append([num for num in section if num != ''])

    df = pd.DataFrame(cleaned)
    df.columns = df.loc[0].tolist()
    return df.drop(0, axis=0)
