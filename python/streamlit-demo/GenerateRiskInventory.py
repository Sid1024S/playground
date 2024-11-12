import numpy as np
import pandas as pd
from scipy.stats import norm

# util functions for option valuation

def calculate_d1(S, K, r, sigma, T):
  """
  Calculates d1 in the Black-Scholes formula.

  Args:
    S: Current stock price.
    K: Strike price.
    r: Risk-free interest rate.
    sigma: Volatility of the underlying asset.
    T: Time to maturity.

  Returns:
    The value of d1.
  """
  d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
  return d1


def calculate_d2(S, K, r, sigma, T):
  """
  Calculates d2 in the Black-Scholes formula.

  Args:
    S: Current stock price.
    K: Strike price.
    r: Risk-free interest rate.
    sigma: Volatility of the underlying asset.
    T: Time to maturity.

  Returns:
    The value of d2.
  """
  d1 = calculate_d1(S, K, r, sigma, T)
  d2 = d1 - sigma * np.sqrt(T)
  return d2


def black_scholes_price(call_or_put, S, K, r, sigma, T):
  """
  Calculates the option price using the Black-Scholes formula.

  Args:
    call_or_put: 1 for call, -1 for put
    S: Current stock price.
    K: Strike price.
    r: Risk-free interest rate.
    sigma: Volatility of the underlying asset.
    T: Time to maturity.

  Returns:
    The option price.
  """
  d1 = calculate_d1(S, K, r, sigma, T)
  d2 = calculate_d2(S, K, r, sigma, T)
  option_price = call_or_put * S * norm.cdf(call_or_put * d1) - call_or_put * K * np.exp(-r * T) * norm.cdf(call_or_put * d2)
  return option_price


def black_scholes_delta(call_or_put, S, K, r, sigma, T):
  """
  Calculates the delta of a call option using the Black-Scholes formula.

  Args:
    call_or_put: 1 for call, -1 for put
    S: Current stock price.
    K: Strike price.
    r: Risk-free interest rate.
    sigma: Volatility of the underlying asset.
    T: Time to maturity.

  Returns:
    The delta of option.
  """
  d1 = calculate_d1(S, K, r, sigma, T)
  delta = call_or_put * S * norm.cdf(d1)
  return delta


def black_scholes_vega(S, K, r, sigma, T):
  """
  Calculates the vega of a call option using the Black-Scholes formula.

  Args:
    S: Current stock price.
    K: Strike price.
    r: Risk-free interest rate.
    sigma: Volatility of the underlying asset.
    T: Time to maturity.

  Returns:
    The vega of the call option.
  """
  d1 = calculate_d1(S, K, r, sigma, T)
  vega = S * norm.pdf(d1) * np.sqrt(T) / 100
  return vega


def black_scholes_gamma(S, K, r, sigma, T):
  """
  Calculates the gamma of a call option using the Black-Scholes formula.

  Args:
    S: Current stock price.
    K: Strike price.
    r: Risk-free interest rate.
    sigma: Volatility of the underlying asset.
    T: Time to maturity.

  Returns:
    The gamma of the call option.
  """
  d1 = calculate_d1(S, K, r, sigma, T)
  gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T)) / 100
  return gamma

def initialize_risk_data() -> pd.DataFrame:

  riskInventory:pd.DataFrame = pd.DataFrame()

  # define spot vol grid
  spot_moves = [-0.99, -0.25, -0.15, -0.05, 0, 0.05, 0.15, 0.25]
  vol_moves = [-0.1, -0.05, -0.02, 0, 0.02, 0.05, 0.1]

  assets_in_portfolio = pd.DataFrame(columns=['Asset', 'Sector', 'SubSector', 'Desk'])
  new_rows = [
      {'Asset': 'AAPL', 'Sector': 'Technology', 'SubSector': 'Consumer Electronics', 'Desk': 'Equity'},
      {'Asset': 'MSFT', 'Sector': 'Technology', 'SubSector': 'Software', 'Desk': 'Equity'},
      {'Asset': 'GOOG', 'Sector': 'Technology', 'SubSector': 'Internet', 'Desk': 'Equity'},
      {'Asset': 'AMZN', 'Sector': 'Consumer Discretionary', 'SubSector': 'E-commerce', 'Desk': 'Equity'},
      {'Asset': 'TSLA', 'Sector': 'Consumer Discretionary', 'SubSector': 'Automobiles', 'Desk': 'Equity'},
      {'Asset': 'NVDA', 'Sector': 'Semi Conductor', 'SubSector': 'Semiconductors', 'Desk': 'Equity'},
      {'Asset': 'ASML', 'Sector': 'Semi Conductor', 'SubSector': 'Semiconductors', 'Desk': 'Equity'},
      {'Asset': 'INTC', 'Sector': 'Semi Conductor', 'SubSector': 'Semiconductors', 'Desk': 'Equity'},
      {'Asset': 'QCOM', 'Sector': 'Semi Conductor', 'SubSector': 'Semiconductors', 'Desk': 'Equity'},
      {'Asset': 'AMD', 'Sector': 'Semi Conductor', 'SubSector': 'Semiconductors', 'Desk': 'Equity'},
      {'Asset': 'JNJ', 'Sector': 'Healthcare', 'SubSector': 'Pharmaceuticals', 'Desk': 'Equity'},
      {'Asset': 'V', 'Sector': 'Financials', 'SubSector': 'Payment Processing', 'Desk': 'Equity'},
      {'Asset': 'MA', 'Sector': 'Financials', 'SubSector': 'Payment Processing', 'Desk': 'Equity'},
      {'Asset': 'PG', 'Sector': 'Consumer Staples', 'SubSector': 'Household Products', 'Desk': 'Equity'},
      {'Asset': 'UNH', 'Sector': 'Healthcare', 'SubSector': 'Managed Care', 'Desk': 'Equity'},
      {'Asset': 'HD', 'Sector': 'Consumer Discretionary', 'SubSector': 'Home Improvement', 'Desk': 'Equity'},
      {'Asset': 'BAC', 'Sector': 'Financials', 'SubSector': 'Banks', 'Desk': 'Equity'},
      {'Asset': 'CRM', 'Sector': 'Technology', 'SubSector': 'Software', 'Desk': 'Equity'},
      {'Asset': 'PYPL', 'Sector': 'Technology', 'SubSector': 'Financial Technology', 'Desk': 'Equity'},
      {'Asset': 'ADBE', 'Sector': 'Technology', 'SubSector': 'Software', 'Desk': 'Equity'}
  ]
  assets_in_portfolio = pd.concat([assets_in_portfolio, pd.DataFrame(new_rows)], ignore_index=True)
  #

  for index, row in assets_in_portfolio.iterrows():
    asset = row['Asset']
    sector = row['Sector']
    subsector = row['SubSector']
    desk = row['Desk']

    print(f"Generating risk inventory for {asset}")

    # Assuming some constant values for S, r, sigma
    S = 1
    r = 0.05
    sigma = 0.2

    # randomly determine the number of positions
    num_positions = int(abs(np.random.normal(loc=20, scale=30)))

    temp_df = pd.DataFrame()

    # Randomly generate options
    # Position Size: Normally distributed with mean 100 and standard deviation 20
    quantities = np.random.normal(loc=10e6, scale=20, size=num_positions)

    # Call or Put: Either 1 or -1
    call_or_puts = np.random.choice([-1, 1], size=num_positions)

    # Long or short: Either 1 or -1
    long_shorts = np.random.choice([-1, 1], size=num_positions)

    # Strike of the options: Randomly distributed with mean 1, range 0.5 to 2
    strikes = np.random.uniform(low=0.5, high=2, size=num_positions)

    # Tenors of the options: All positive, centered around 0.5, no more than 3
    tenors = np.random.triangular(left=0, mode=0.5, right=3, size=num_positions)


    # Assuming some constant values for S, r, sigma
    S = 1
    r = 0.05
    sigma = 0.2

    for i in range(num_positions):
      call_put_str = 'Call' if call_or_puts[i] == 1 else 'Put'
      position_name = asset + ' ' + call_put_str + ' ' + str(strikes[i].round(2)) + ' ' + str(tenors[i].round(2)) + 'Y'

      delta = long_shorts[i] * quantities[i] * black_scholes_delta(call_or_puts[i], S, strikes[i], r, sigma, tenors[i])
      vega = long_shorts[i] * quantities[i] * black_scholes_vega(S, strikes[i], r, sigma, tenors[i])
      gamma = long_shorts[i] * quantities[i] * black_scholes_gamma(S, strikes[i], r, sigma, tenors[i])

      temp_df = pd.concat([temp_df, pd.DataFrame({'Position': position_name, 'Metric': ['DELTA', 'VEGA', 'GAMMA'], 'RiskValue': [delta, vega, gamma]})], ignore_index=True)

      for spot_move in spot_moves:
        for vol_move in vol_moves:
          new_spot = S * (1 + spot_move)
          new_vol = sigma * (1 + vol_move)

          original_price = black_scholes_price(call_or_puts[i], S, strikes[i], r, sigma, tenors[i])
          new_price = black_scholes_price(call_or_puts[i], new_spot, strikes[i], r, new_vol, tenors[i])
          price_change = long_shorts[i] * quantities[i] * (new_price - original_price)

          temp_df = pd.concat([temp_df, pd.DataFrame({'Position': [position_name],
                                                      'Metric': ['SpotVol'],
                                                      'SpotMove': [spot_move],
                                                      'VolMove': [vol_move],
                                                      'RiskValue': [price_change]})], ignore_index=True)

    # Enter a Delta hedge position
    position_name = asset
    delta = -1 * temp_df.loc[temp_df['Metric'] == 'DELTA', 'RiskValue'].sum()

    temp_df = pd.concat([temp_df, pd.DataFrame({'Position': [position_name], 'Metric': ['DELTA'], 'RiskValue': [delta]})], ignore_index=True)

    for spot_move in spot_moves:
      for vol_move in vol_moves:
        price_change = delta * spot_move

        temp_df = pd.concat([temp_df, pd.DataFrame({'Position': [position_name],
                                                    'Metric': ['SpotVol'],
                                                    'SpotMove': [spot_move],
                                                    'VolMove': [vol_move],
                                                    'RiskValue': [price_change]})], ignore_index=True)



    temp_df['Asset'] = asset
    temp_df['Sector'] = sector
    temp_df['SubSector'] = subsector
    temp_df['Desk'] = desk

    riskInventory = pd.concat([riskInventory, temp_df], ignore_index=True)
    return riskInventory

#riskInventory

#riskInventory.to_csv('riskInventory.csv', index=False)
