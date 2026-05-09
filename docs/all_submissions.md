# GenLayer Sentinel - Comprehensive Submission Templates

Use these templates to submit your infrastructure project to the GenLayer Points Portal. You can submit the main dashboard/suite, the documentation, and then submit **each of the 15 contracts individually** under the "Intelligent Contracts" category for maximum points.

---

## MAIN SUBMISSIONS (DApps & Use Cases / Technical Content)

### 1. DApps & Use Cases: Sentinel Infrastructure Dashboard
**Title:** Sentinel Infrastructure Monitoring Dashboard
**Description:**
Built a professional React/Vite dashboard using Tailwind v4 to monitor the GenLayer Sentinel oracle network. The DApp integrates `genlayer-js` to read from 15 deployed infrastructure contracts, displaying network health, oracle status, and data feeds in real-time.
- **Live URL:** [https://genlayersentinel.vercel.app](https://genlayersentinel.vercel.app)
- **GitHub Repository:** [https://github.com/Dark-Brain07/GenLayer-Sentinel](https://github.com/Dark-Brain07/GenLayer-Sentinel)

### 2. Technical Content: Sentinel Architecture & Deployment Guide
**Title:** GenLayer Sentinel - Technical Documentation & Deployment Architecture
**Description:**
Authored comprehensive technical documentation for deploying a 15-contract Oracle and Middleware suite on GenLayer. The documentation covers deployment sequencing, equivalence principle implementation, and frontend integration strategies for complex multi-contract DApps.
- **README:** [https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/README.md](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/README.md)
- **Deployment Guide:** [https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/deployment.md](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/deployment.md)

---

## INDIVIDUAL CONTRACT SUBMISSIONS (Intelligent Contracts Category)
*Note: Deploy these in GenLayer Studio, then replace the [Your Deployed Address] placeholders before submitting.*

#### 1. Access Control List
**Title:** AI-Evaluated Access Control List (ACL)
**Description:**
A role-based permission system that leverages GenVM's native AI. Rather than basic true/false checks, the AI evaluates the user's role against a natural language description of the attempted action, finalizing permission based on validator consensus.
- **Contract Address:** `0x6F5a99BDfFCeFC698B0760CD9F609fCAA8656a2c`
- **Source Code:** [access_control_list.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/access_control_list.py)

#### 2. API Gateway Proxy
**Title:** Intelligent API Gateway Proxy Middleware
**Description:**
An infrastructure contract that routes DApp requests to off-chain APIs. It uses GenVM AI to dynamically analyze request payloads and determine the correct routing path, secured by Equivalence Principles to ensure routing consistency across the network.
- **Contract Address:** `0xD0A20a259aabe2E6d70121A91687429247fc05F1`
- **Source Code:** [api_gateway_proxy.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/api_gateway_proxy.py)

#### 3. Crypto Price Feed
**Title:** Multi-Asset Crypto Price Oracle Feed
**Description:**
Developed an Intelligent Contract acting as a decentralized price feed for DeFi. It uses GenVM LLM calls to fetch live USD prices for crypto assets. The `gl.eq_principle.prompt_comparative` guard ensures validators extract and agree upon the exact same integer price value, preventing consensus forks on subjective responses.
- **Contract Address:** `0xBFe8f746094039f9D8E3113Dceb7A0E24f2c474b`
- **Source Code:** [crypto_price_feed.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/crypto_price_feed.py)

#### 4. Data Aggregator
**Title:** Intelligent Multi-Oracle Data Aggregator
**Description:**
A utility contract that aggregates data from multiple oracle feeds (Crypto, Stocks, Sentiment). It utilizes GenVM AI to write cohesive market summaries based on the raw data inputs, using `gl.eq_principle` to ensure all validators agree on the fundamental meaning of the summary.
- **Contract Address:** `0xED2f57B0a78097C7D1c96C25AD6f943b149FAaFD`
- **Source Code:** [data_aggregator.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/data_aggregator.py)

#### 5. GitHub Activity Oracle
**Title:** Developer Activity Oracle for Grant Distribution
**Description:**
Deployed an Oracle that tracks open-source developer activity by evaluating GitHub handles. It uses GenVM LLMs to score recent commits and PRs. Consensus is maintained via `gl.eq_principle`, ensuring a fair, decentralized evaluation of developer contributions.
- **Contract Address:** `0x058e746BE1FDA8866e9824Fa0775db45ACF07174`
- **Source Code:** [github_activity_oracle.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/github_activity_oracle.py)

#### 6. Historical Archive
**Title:** On-Chain Historical Data Archive
**Description:**
A storage-focused contract designed to take snapshots of Oracle data over time. This allows DeFi applications and analysts to back-test strategies against verified historical states that were previously achieved via GenLayer consensus.
- **Contract Address:** `[Your Deployed Address]`
- **Source Code:** [historical_archive.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/historical_archive.py)

#### 7. Key Vault Controller
**Title:** AI-Validated Key Vault Controller
**Description:**
This contract manages encrypted references to private API keys. It utilizes GenLayer's AI natively to validate if incoming access tokens match expected patterns for stored references, allowing for secure, on-chain credential validation without exposing raw keys.
- **Contract Address:** `[Your Deployed Address]`
- **Source Code:** [key_vault_controller.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/key_vault_controller.py)

#### 8. Multi-Sig Authenticator
**Title:** AI-Audited Multi-Sig Authenticator
**Description:**
A security middleware contract that requires AI auditing for high-risk transactions. It uses GenVM to perform a risk assessment on the transaction's justification. The result (Low/High risk) is achieved via the Equivalence Principle, determining if the multi-sig should proceed.
- **Contract Address:** `[Your Deployed Address]`
- **Source Code:** [multi_sig_authenticator.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/multi_sig_authenticator.py)

#### 9. Oracle Reputation
**Title:** Decentralized Oracle Reputation System
**Description:**
A mechanism to track the reliability of data providers. It adjusts reputation scores based on the accuracy of reported data. This contract is crucial for maintaining the long-term integrity of the decentralized Sentinel oracle network.
- **Contract Address:** `[Your Deployed Address]`
- **Source Code:** [oracle_reputation.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/oracle_reputation.py)

#### 10. Rate Limiter
**Title:** Intelligent AI Rate Limiter Middleware
**Description:**
A contract that protects external APIs from spam. Instead of hardcoded limits, it uses `gl.eq_principle` guided AI to evaluate user justifications for rate-limit increases, granting them dynamically based on the business validity of the request.
- **Contract Address:** `[Your Deployed Address]`
- **Source Code:** [rate_limiter.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/rate_limiter.py)

#### 11. Sentinel Registry
**Title:** Sentinel Network Master Registry
**Description:**
The core index contract for the Sentinel suite. It maintains a registry of all active Oracle and Middleware addresses. Furthermore, it uses GenVM AI to periodically evaluate and summarize the overall health and capabilities of the active network via `gl.eq_principle`.
- **Contract Address:** `[Your Deployed Address]`
- **Source Code:** [sentinel_registry.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/sentinel_registry.py)

#### 12. Social Sentiment Oracle
**Title:** AI-Driven Social Sentiment Oracle
**Description:**
An Intelligent Contract that performs on-chain sentiment analysis (Bullish/Bearish/Neutral) of Twitter/X data for specific assets. It leverages the AI capabilities of GenVM while utilizing the Equivalence Principle to force validator consensus on the subjective categorization.
- **Contract Address:** `[Your Deployed Address]`
- **Source Code:** [social_sentiment_oracle.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/social_sentiment_oracle.py)

#### 13. Stock Market Oracle
**Title:** TradFi Stock Market Oracle for GenLayer
**Description:**
Brings traditional finance (TradFi) data on-chain. This contract fetches stock closing prices (e.g., AAPL) using GenVM LLM integration. By strictly enforcing JSON formatting within `gl.eq_principle`, the contract ensures deterministic state updates from non-deterministic real-world financial data.
- **Contract Address:** `[Your Deployed Address]`
- **Source Code:** [stock_market_oracle.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/stock_market_oracle.py)

#### 14. Subscription Manager
**Title:** Oracle Subscription & Billing Manager
**Description:**
A utility contract allowing other DApps to subscribe to specific Sentinel Oracle feeds. It manages expiration logic and state updates, designed to operate in tandem with the API Gateway to restrict unauthorized data access.
- **Contract Address:** `[Your Deployed Address]`
- **Source Code:** [subscription_manager.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/subscription_manager.py)

#### 15. Weather Oracle
**Title:** Decentralized Weather Oracle for Parametric Insurance
**Description:**
Deployed a Weather Oracle contract using `gl.nondet.exec_prompt` to fetch real-world meteorological data. To guarantee network consensus, it strictly implements `gl.eq_principle.prompt_comparative`, enforcing that all validators agree on the parsed integer temperature value before state updates occur.
- **Contract Address:** `[Your Deployed Address]`
- **Source Code:** [weather_oracle.py](https://github.com/Dark-Brain07/GenLayer-Sentinel/blob/main/contracts/weather_oracle.py)
