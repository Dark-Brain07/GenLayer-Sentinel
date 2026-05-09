# GenLayer Sentinel
**The Decentralized Oracle & Security Middleware Suite for GenLayer**

GenLayer Sentinel is a massive infrastructure project consisting of **15 Expert Intelligent Contracts**. It is designed to provide a robust, AI-driven foundation for DApps requiring off-chain data, secure API management, and complex cross-contract consensus on the GenLayer network.

## The GenVM Consensus Challenge
When building decentralized oracles, the standard blockchain dilemma applies: how do independent nodes agree on real-world data at an exact moment in time? In GenLayer, this is complicated by the use of LLMs (`gl.nondet.exec_prompt`), which are inherently non-deterministic. If two validators ask an LLM for the weather, they might get slightly different text responses, causing a consensus failure.

**The Sentinel Solution:** Every contract in this suite strictly implements the **Equivalence Principle** (`gl.eq_principle.prompt_comparative`). By constraining the AI outputs to strict JSON formats and defining logical equivalence (e.g., "Both outcomes must yield the exact same integer value"), Sentinel ensures perfect network consensus across 15 distinct microservices.

---

## Technical Architecture

The 15 Intelligent Contracts are divided into three highly specialized layers:

### Layer 1: Data Oracles (The "Sensors")
These contracts handle the secure fetching of off-chain data.
1. **`weather_oracle.py`**: Fetches meteorological data, essential for on-chain parametric insurance DApps.
2. **`crypto_price_feed.py`**: Aggregates cryptocurrency prices, forming the backbone of GenLayer DeFi.
3. **`stock_market_oracle.py`**: Bridges Traditional Finance (TradFi) stock market data on-chain.
4. **`social_sentiment_oracle.py`**: Uses GenVM AI to read Twitter/X data and classify asset sentiment as Bullish, Bearish, or Neutral.
5. **`github_activity_oracle.py`**: Analyzes developer repositories to automate decentralized grant distributions based on actual code contributions.

### Layer 2: Security & Privacy (The "Shield")
Blockchain transparency often exposes sensitive data like API keys. This layer mitigates those risks using AI-evaluated middleware.
6. **`api_gateway_proxy.py`**: Routes incoming DApp requests to the correct oracle, hiding internal logic.
7. **`key_vault_controller.py`**: Stores encrypted references to API keys and uses AI to validate token patterns, avoiding plaintext key exposure.
8. **`rate_limiter.py`**: Prevents API spam. Uniquely, it uses AI to read user justifications for rate-limit increases and approves them dynamically if valid.
9. **`access_control_list.py`**: Replaces hardcoded true/false role checks with AI evaluations of user roles against requested natural-language actions.
10. **`multi_sig_authenticator.py`**: Analyzes the "risk level" of a transaction justification using AI before deciding if the multi-sig approval process can proceed.

### Layer 3: Utility & Logic (The "Brain")
These contracts manage the ecosystem, subscriptions, and historical state.
11. **`data_aggregator.py`**: Ingests data from multiple oracles and uses AI to write a cohesive, consensus-verified market summary.
12. **`subscription_manager.py`**: Handles DApp subscriptions and billing durations for access to the Sentinel network.
13. **`historical_archive.py`**: Takes state snapshots of oracle data, providing a verifiable timeline for back-testing trading strategies.
14. **`oracle_reputation.py`**: Tracks node accuracy and penalizes validators/nodes that supply malicious or consistently incorrect data.
15. **`sentinel_registry.py`**: The master directory that indexes all active contracts and uses AI to generate an overall "Network Health" status report.

---

## The Sentinel Dashboard
The project includes a highly polished React/Vite dashboard deployed on Vercel. 
- It uses `genlayer-js` to connect to the GenLayer testnet.
- It provides a comprehensive UI to monitor the status, health, and recent data of all 15 Intelligent Contracts simultaneously.

### Running the Dashboard Locally
```bash
cd dashboard
npm install
npm run dev
```

## Contributing
When contributing to GenLayer Sentinel, ensure all new intelligent contracts utilize the `gl.eq_principle` to maintain the integrity of the network's consensus mechanism.
