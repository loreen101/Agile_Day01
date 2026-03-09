# Task1: Sum of Digits

This Python project extracts **individual digits from a text string** and calculates their **total sum**.

The program uses **Regular Expressions (Regex)** to find digits and **pytest** to test the functionality.

---

## Project Structure


- `Sum_of_Digits.py` → Main program that extracts digits and calculates their sum  
- `test_calculate_sum_of_digits.py` → Unit tests using pytest  
- `test_results.txt` → Pytest output confirming that all test cases passed successfully  
- `README.md` → Project documentation  

---

## Features

- Extracts digits from text using **Regex**
- Counts **each digit individually**
- Handles multiple edge cases
- Includes **10 pytest unit tests**

Example:

```
Input:  a12b34
Digits: 1 + 2 + 3 + 4
Output: 10
```

---

## Installation

Clone the repository or download the project files.

Then install **pytest**:

```bash
pip install pytest
```

Verify installation:

```bash
pytest --version
```

---

## Running the Program

Run the main script:

```bash
python Sum_of_Digits.py
```

Example:

```
Enter text: a1b2c3
Extracted digits: [1, 2, 3]
Total Sum of Digits: 6
```

---

## Running Tests

Run all tests in the project folder:

```bash
pytest
```

For detailed output:

```bash
pytest test_sum_of_digits.py -v
```

Example output:

```
collected 10 items

test_calculate_sum_of_digits.py .......... [100%]

10 passed
```

---

## Test Cases Covered

The tests check multiple scenarios:

- Simple digits
- Multiple digit numbers
- No digits in text
- Digits at beginning or end
- Empty string
- Consecutive digits
- Digits separated by spaces
- Leading zeros
- Single digit
- Mixed characters

---

## Technologies Used

- Python
- Regular Expressions (`re`)
- pytest for testing

---

# Task2: CI/CD Tools Comparison (Jenkins vs AWS CodePipeline vs GitHub Actions)

## 1. Business Use Cases — When to Use

### Jenkins
- Large enterprises needing **full control** over their CI/CD infrastructure.
- Teams with complex, highly customized build pipelines that no hosted solution can satisfy.
- Organizations running workloads **on-premises** or in air-gapped / regulated environments.
- Projects that rely on a vast plugin ecosystem (1,800+ plugins) for integration with virtually any tool.

### AWS CodePipeline
- Teams already invested in the **AWS ecosystem** (EC2, ECS, EKS, Lambda, S3, etc.).
- Organizations that want a **fully managed** service with zero infrastructure to maintain.
- Workloads where tight integration with AWS services (CloudFormation, CodeBuild, CodeDeploy) is a priority.
- Regulated industries that need to stay within a single cloud provider for compliance.

### GitHub Actions
- Teams whose source code already lives on **GitHub**.
- Open-source projects that benefit from **free CI/CD minutes** on public repositories.
- Startups and small-to-mid teams that want a **quick, low-friction** setup with minimal configuration.
- Projects that value a large community **marketplace of reusable actions**.

---

## 2. Pricing

### Jenkins
| Aspect | Details |
|---|---|
| License | **Free & open-source** (MIT License) |
| Infrastructure | Self-hosted — you pay for your own servers, storage, and networking |
| Maintenance | Requires dedicated DevOps effort for upgrades, scaling, and plugin management |
| Hidden costs | Hardware, electricity, sysadmin time, and plugin compatibility overhead |

> **Bottom line:** No license fee, but total cost of ownership can be significant at scale.

### AWS CodePipeline
| Aspect | Details |
|---|---|
| Pipelines | **$1.00 per active pipeline per month** (free tier: 1 free pipeline for 12 months) |
| CodeBuild | Pay per **build minute** — starts at $0.005/min (general1.small Linux) |
| CodeDeploy | Free for deployments to EC2/Lambda; charges apply for on-premises instances |
| Data transfer | Standard AWS data-transfer rates apply |

> **Bottom line:** Pay-as-you-go; cost-effective for AWS-centric workloads, but build-minute costs can grow with heavy usage.

### GitHub Actions
| Aspect | Details |
|---|---|
| Public repos | **Free** — unlimited minutes |
| Private repos (Free plan) | **2,000 minutes/month** included |
| Private repos (Team plan) | **3,000 minutes/month** included |
| Private repos (Enterprise) | **50,000 minutes/month** included |
| Overage | ~$0.008/min (Linux), ~$0.016/min (Windows), ~$0.08/min (macOS) |
| Self-hosted runners | **Free** — you provide the infrastructure |

> **Bottom line:** Very generous free tier, especially for open-source; costs are predictable and scale with usage.

---

## 3. Deployment Settings

### Jenkins
- **Where it runs:** Self-hosted on bare metal, VMs, Docker containers, or Kubernetes.
- **OS support:** Linux, Windows, macOS — anywhere a JVM runs.
- **Pipeline definition:** `Jenkinsfile` (Declarative or Scripted Groovy DSL) stored in the repo.
- **Agents/Nodes:** Supports distributed builds via permanent or cloud-provisioned agents.
- **Scaling:** Manual or plugin-assisted (e.g., Kubernetes plugin for dynamic pod agents).
- **Security:** Full responsibility on the operator — network policies, RBAC, secrets management via plugins like HashiCorp Vault.

### AWS CodePipeline
- **Where it runs:** Fully managed within **AWS cloud** — no servers to provision.
- **Pipeline definition:** JSON/YAML via the AWS Console, CLI, CloudFormation, or CDK.
- **Build environment:** AWS CodeBuild provides managed build containers (or custom Docker images).
- **Deploy targets:** EC2, ECS, EKS, Lambda, S3, Elastic Beanstalk, and on-premises via CodeDeploy agent.
- **Scaling:** Automatic — AWS handles capacity.
- **Security:** IAM roles & policies, KMS encryption, VPC integration, and AWS CloudTrail auditing.

### GitHub Actions
- **Where it runs:** GitHub-hosted runners (Ubuntu, Windows, macOS) **or** self-hosted runners on your own infrastructure.
- **Pipeline definition:** YAML workflow files stored in `.github/workflows/`.
- **Triggers:** Push, PR, schedule (cron), manual dispatch, repository dispatch, and 30+ event types.
- **Deploy targets:** Any target reachable from the runner — cloud providers, Kubernetes, FTP, SSH, etc.
- **Scaling:** GitHub-hosted runners scale automatically; self-hosted runners scale as you configure them.
- **Security:** Encrypted secrets per repo/org/environment, OIDC for cloud auth, environment protection rules, and required reviewers.

---

## Quick Summary

| Criteria | Jenkins | AWS CodePipeline | GitHub Actions |
|---|---|---|---|
| **Best for** | Full control & complex pipelines | AWS-native workloads | GitHub-hosted projects & OSS |
| **Hosting** | Self-hosted | Fully managed (AWS) | Hosted + self-hosted option |
| **Pricing model** | Free (OSS) + infra costs | Pay-per-pipeline + build mins | Free tier + per-minute overage |
| **Setup complexity** | High | Medium | Low |
| **Plugin/Extension ecosystem** | 1,800+ plugins | AWS service integrations | 20,000+ marketplace actions |
| **Scaling** | Manual / plugin-based | Automatic | Automatic (hosted) |
