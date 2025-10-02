import ffbot
import pandas as pd

# Define your three leagues
leagues = [
    {
        "name": "Quadruple Option!",
        "league_id": 100351,
        "team_id": 11,
        "positions": "QB, WR, WR, WR, RB, RB, TE, W/R/T, K, DEF, BN, BN, BN, BN, IR"
    },
    {
        "name": "Decapitators",
        "league_id": 1223948,  # Replace with your actual league ID
        "team_id": 3,  # Replace with your actual team ID
        "positions": "QB, WR, WR, WR, RB, RB, TE, W/R/T, K, DEF, BN, BN, BN, BN, IR"
    },
    {
        "name": "Juicemen",
        "league_id": 1476297,  # Replace with your actual league ID
        "team_id": 7,  # Replace with your actual team ID
        "positions": "QB, WR, WR, WR, RB, RB, TE, W/R/T, K, DEF, BN, BN, BN, BN, IR"
    }
]

week = ffbot.current_week()
print(f"Processing Week {week}...\n")

# Process each league
for league_config in leagues:
    print(f"\n{'='*60}")
    print(f"Processing {league_config['name']} (ID: {league_config['league_id']})")
    print(f"{'='*60}\n")
    
    try:
        # Scrape player data
        df = ffbot.scrape(league_config['league_id'])
        
        # Fill NaN values
        week_columns = [f"Week {i}" for i in range(week, 18)]
        for col in week_columns:
            if col in df.columns:
                df[col] = df[col].fillna(0)
        
        # Optimize
        df_opt = ffbot.optimize(
            df, 
            week, 
            league_config['team_id'], 
            league_config['positions']
        )
        
        # Display results
        print(f"\n{league_config['name']} Recommendations:")
        print(df_opt)
        print("\n")
        
        # Optionally save results
        df_opt.to_csv(f"league_{league_config['league_id']}_week_{week}_recommendations.csv", index=False)
        print(f"Saved to league_{league_config['league_id']}_week_{week}_recommendations.csv")
        
    except Exception as e:
        print(f"Error processing {league_config['name']}: {e}")
        continue

print("\nAll leagues processed!")
