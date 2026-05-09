# GenLayer Sentinel
**The Decentralized Oracle & Security Middleware Suite for GenLayer**

GenLayer Sentinel is a massive infrastructure project consisting of **15 Expert Intelligent Contracts** categorized into three layers: Data Oracles, Security & Privacy, and Utility Logic. It provides a robust foundation for DApps requiring off-chain data, secure API management, and complex cross-contract consensus.

## Architecture

### Layer 1: Data Oracles (Sensors)
Uses `gl.nondet.exec_prompt` to fetch real-world data and `gl.eq_principle` to ensure cross-validator consensus.
- `weather_oracle.py`: Parametric insurance data.
- `crypto_price_feed.py`: DeFi price aggregation.
- `stock_market_oracle.py`: TradFi data bridging.
- `social_sentiment_oracle.py`: Twitter/X sentiment analysis.
- `github_activity_oracle.py`: Developer activity tracking.

### Layer 2: Security & Privacy (Shield)
- `api_gateway_proxy.py`: Secure routing for off-chain APIs.
- `key_vault_controller.py`: Encrypted key reference management.
- `rate_limiter.py`: AI-evaluated rate limit increases.
- `access_control_list.py`: Role-based permission evaluation.
- `multi_sig_authenticator.py`: AI-audited transaction approvals.

### Layer 3: Utility & Logic (Brain)
- `data_aggregator.py`: Combines multiple feeds.
- `subscription_manager.py`: Manages DApp subscriptions.
- `historical_archive.py`: Stores snapshots for back-testing.
- `oracle_reputation.py`: Tracks node accuracy.
- `sentinel_registry.py`: The master index.

## Dashboard
The project includes a React/Vite dashboard to monitor the entire Oracle network in real-time.

## Setup & Run
```bash
cd dashboard
npm install
npm run dev
```
