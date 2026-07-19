# Business Problem Definition

## Business Context

A retail bank receives loan applications from customers every day. Before approving a loan, the institution must assess the applicant's credit risk to minimize financial losses while maintaining a healthy approval rate.

The current decision process combines business rules with human analysis. However, manual evaluation becomes increasingly difficult as the number of applications grows.

This project proposes a Machine Learning solution that estimates the probability of customer default, supporting credit analysts during the credit approval process.

---

## Problem Statement

How can Machine Learning help estimate the probability that a customer will default on a loan?

The objective is not to replace human analysts, but to provide an additional decision-support tool capable of improving consistency and reducing financial risk.

---

## Stakeholders

- Credit Analysts
- Credit Risk Department
- Retail Banking Managers

---

## Business Objective

Develop a classification model capable of estimating the probability of customer default and supporting loan approval decisions.

---

## Machine Learning Objective

Predict whether a customer is likely to become a bad payer based on historical financial and demographic information.

Target Variable:

- Good Credit
- Bad Credit

---

## Success Criteria

Business

- Reduce financial losses caused by high-risk approvals.
- Support analysts with consistent risk scores.
- Improve credit approval quality.

Technical

- Compare multiple Machine Learning models.
- Optimize the decision threshold according to business costs.
- Build a reproducible MLOps pipeline.

---

## Business Risks

False Positive

Rejecting a reliable customer.

Impact:

- Lost business opportunity.
- Customer dissatisfaction.

False Negative

Approving a high-risk customer.

Impact:

- Financial loss.
- Higher default rates.

For this project, False Negatives are considered significantly more costly than False Positives.

---

## Assumptions

- Historical customer information contains predictive patterns.
- The dataset is representative of the business problem.
- The model supports decision-making but does not replace human judgment.

---

## Project Scope

Included

- Data exploration
- Feature Engineering
- Model Training
- Explainability
- Deployment
- Monitoring

Not Included

- Real-time integration with banking systems.
- Production database integration.
- Loan pricing optimization.
