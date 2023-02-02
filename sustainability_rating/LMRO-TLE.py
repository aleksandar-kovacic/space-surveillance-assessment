import pandas as pd
#df = pd.read_excel("discos_database_complete.xlsx")
df = pd.read_excel("database/SDDB_without_LEO_bLEO_DB_test_vollständig.xlsx")

print(df["objectClass"].unique())

objectClass = [
    "Payload", "Rocket Body", "Payload Mission Related Object", 
    "Rocket Mission Related Object", "Other Mission Related Object",
    "Rocket Debris", "Payload Debris"
]

df = df[df['objectClass'].isin(objectClass)]
df.reset_index(drop = True, inplace=True)
print(df)

df.to_excel("../../../r4c_simulation-beta/user_input/database/ARES_R4C_validation_database.xlsx")