from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",
                           total_tasks=data.total_tasks_completed,
                           satisfaction=data.satisfaction_score,
                           weekly_tasks=data.tasks_by_week,
                           monthly_engagement=data.engagement_by_month,
                           category_tasks=data.tasks_by_category
                              )

if __name__ == "__main__":
    app.run(debug=True)
