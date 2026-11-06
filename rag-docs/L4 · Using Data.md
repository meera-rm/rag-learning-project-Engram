# Lesson 4 — Using Data

How you split, rebalance, version and validate data decides whether your evaluation tells the truth about production — so choose splits based on how records are related and what the model will face live.

## 1. Dataset roles: train, validation, test

- **Train** — what the model learns from.
- **Validation** — what you check against while iterating (choosing features, hyperparameters, models).
- **Test** — a final, independent check after development.

Size splits by **record counts**, not habit: with 1,000 tickets, a 100-record test set means one reclassified ticket moves accuracy by a full point; with 2,000,000 tickets, 98/1/1 still gives 20,000 test records. Make sure rare classes have enough examples in val/test.

**Keep the test set independent:** if you look at it more than two or three times, it has quietly become another validation set.

**Extra evaluation sets** (only when they answer a distinct question): final holdout, slice set (an important segment), stress set (hard/extreme cases), regression set (fixed bugs that must stay fixed), gold set (small, carefully reviewed, high-confidence labels).

## 2. Split strategies

Dataset roles are the buckets; split strategies decide **how records enter** them.

| Strategy | Use when | Protects against | Limitation |
| --- | --- | --- | --- |
| Uniform random | Rows fully independent | Manual selection bias | Fails if any dependency exists |
| Stratified | Rare labels need coverage | Classes vanishing from a split | Doesn't handle time or groups |
| Time-based | Future differs from past | Future-to-past leakage | Sensitive to cutoff choice |
| Grouped | Same entity appears many times | Entity leakage | Big groups distort sizes |
| Cluster-aware | No group key, but near-duplicates | Near-duplicate inflation | Depends on similarity threshold |

- **Stratified** should be your default: apply 80/10/10 inside every stratum (e.g. customer × HTTP method) so even 10 DELETE requests split 8/1/1.
- **Time-based:** Jan–Sep train, Oct–Nov validation, Dec test. Exclude records created before the cutoff whose **label arrived after** it.
- **Grouped:** all of Customer A's 12 tickets go to the same split.
- **Combine:** keep customers together (hard boundary) while *approximating* class coverage (goal) — never split a customer just to hit exact percentages.

**The holdout defines the question:** holding out later tickets asks "can it route *future* tickets from *known* customers?"; holding out customers asks "can it handle *new* customers?" To test both, hold out later periods *and* unseen customers.

**Real-world example:** Random-splitting a customer's 40 near-identical "password reset" tickets puts copies in train and test; accuracy looks 97% but drops to 80% on new customers.

## 3. Rebalancing the training set

With Billing 80K, Access 12K, Security 800, a model can predict "Billing" always and still look strong. First ask: are rare labels accurate? Does the imbalance reflect reality or a collection gap? Must each small class be detected separately? What do misses cost vs false alarms? Can we collect more data?

**Split first, then rebalance only the training set** — validation and test keep the real distribution.

| Method | What changes | Use when | Risk |
| --- | --- | --- | --- |
| Oversampling | Rare examples shown more often | Rare labels are trustworthy but too infrequent | Memorising repeats; no new diversity |
| Undersampling | Use a subset of majority class | Majority is abundant/repetitive | Discards useful variation |
| Weighted learning | Errors on rare classes cost more (e.g. `class_weight`) | Model supports weights; keep all data | Bad weights skew tradeoffs; noise amplified |
| Synthetic data | Add generated rare-class examples | Real examples scarce, generation plausible | Artifacts, false diversity |

No rebalancing method fixes bad labels or missing real-world diversity.

## 4. Versioning and reproducibility

Version every step: source snapshot and extraction date, cleaning and label versions, filters and exclusions, split method and constraints, random seed, rebalancing rules, eval-set definitions.

Save a **split manifest** — one record per data row:

```json
{"ticket_id": "TKT-10042", "split_role": "train", "group_id": "cust_8a4f",
 "excluded": false, "exclusion_reason": null, "split_policy_version": "v3"}
```

**Fixed benchmark:** every model candidate is scored on the same split. If you add data or change the split, that is a **new benchmark** and results are not directly comparable.

**Real-world example:** "Run 017 = Tickets v4 (extracted Jul 1) + Cleaning policy v2 + Labels v3 + Grouped split v3 + seed 42". Anyone can rebuild exactly what that model saw.

## 5. Small datasets and cross-validation

With 100 labeled records, an 80/10/10 split leaves only 80 to learn from, and one changed prediction swings validation accuracy by 10 points. **K-fold cross-validation** rotates the validation fold k times and averages results, so every development record is used for both training and validation.

| Variant | Use when |
| --- | --- |
| Standard k-fold | Independent rows, balanced classes |
| Stratified k-fold | Rare labels must appear in every fold |
| Grouped k-fold | Same customer/incident must stay together |
| Repeated CV | Measuring sensitivity to fold assignment |
| Time-aware (forward) CV | Train on earlier chunks, evaluate on the next one; future never trains |

- Match the CV variant to your split strategy. k is usually limited by your rarest class.
- **Fold first, then rebalance** inside the training folds — oversampling before folding puts copies of the same ticket in train and validation.
- After CV: keep a final test set outside the folds, pick the approach from fold results, retrain on all development data, evaluate **once** on test. Record per-fold and aggregate stats.

## 6. Operational validation (data contracts in production)

Recurring checks that stop bad inputs reaching the model: **define expectations → validate each record → monitor over time.**

| Expectation | Allowed | If violated |
| --- | --- | --- |
| Required fields | Present, non-empty | Reject or request correction |
| Type/format | Parseable as declared type | Reject or quarantine |
| Categories | Documented set or explicit "unknown" | Map to unknown or reject |
| Numeric values | Within min/max | Reject or approved correction |
| Schema version | Supported version | Convert or reject |
| Input size | Within record/token/context limits | Approved reduction (e.g. summarise) or reject |

Monitor the incoming population: a new channel value (`chat-v2`), language null rate rising from 2%, a 10× spike in auto-generated tickets, Security tickets jumping from 8% to 19% — each triggers investigation and a defined response.

## Top resources

- [scikit-learn: Cross-validation guide](https://scikit-learn.org/stable/modules/cross_validation.html) — official docs for `StratifiedKFold`, `GroupKFold`, `TimeSeriesSplit` and `StratifiedGroupKFold`, i.e. every split strategy in this lesson as code.
- [imbalanced-learn docs](https://imbalanced-learn.org/) — the standard library for over/undersampling (incl. SMOTE) with pipelines that rebalance correctly inside CV folds.
- [Great Expectations](https://docs.greatexpectations.io/) or [Pandera](https://pandera.readthedocs.io/) — tools for writing data contracts as code; directly useful for the operational-validation step and common in data-engineering roles.
- [DVC (Data Version Control)](https://dvc.org/doc) — versions datasets and pipelines alongside Git, making the "Run 017" style reproducibility practical.
- *Designing Machine Learning Systems* (Chip Huyen), Ch. 4–6 — strong practical discussion of data leakage, class imbalance and evaluation splits.
