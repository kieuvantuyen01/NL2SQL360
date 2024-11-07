from nl2sql360.core import Core
from nl2sql360.arguments import CoreArguments, EvaluationArguments

if __name__ == "__main__":
    core_args = CoreArguments()

    core = Core(core_args)

    evaluation_args = EvaluationArguments(
        eval_name="C3_SQL_2",
        eval_dataset="spider_dev",
        # eval_metrics=["ex", "em", "ves"],
        eval_metrics=["ex", "em"],
        pred_sqls_file="./tests/predict_sqls/spider_dev/C3_SQL.sql",
        enable_spider_eval=True
    )

    core.evaluate(evaluation_args)
