# SET FN Call
mymodel = models["Naive"]
y_pred = models["Naive"].predict(X_test)
y_probas = mymodel.predict_proba(X_test)
probas_dict = {
    key: model_k.predict_proba(X_test) for key, model_k in models.items()
}
models["Naive"].classes_
y_true = y_test
classes_to_plot = None

probas_dict = {"a": models["Naive"].predict_proba(X_test)}

probas_dict = {
    model_i: models[model_i].predict_proba(X_test) for model_i in models
}


# cool
def roc_helper(model_label, y_true, probas_i, pos_label):
    roc_tuple = metrics.roc_curve(y_true, probas_i, pos_label=pos_label)
    roc_tuple = (model_label,) + (pos_label,) + roc_tuple  #tuple concat
    return dict(zip(["model", "class", "fpr", "tpr", "thresholds"], roc_tuple))


#fpr, tpr, thresholds = metrics.roc_curve(y_true, probas)
#toy = list(map(lambda x: metrics.roc_curve(y_true, x), probas.T))

toy = []
for model_label, probas_model in probas_dict.items():
    toy_i = [
        roc_helper(model_label, y_true, probas_i, classes[i])
        for i, probas_i in enumerate(probas_model.T)
        if i in indices_to_plot
    ]
    toy = toy + toy_i

# Heavy lifting done above, here just need to concatenate all together
toy_listdf = [pd.DataFrame(roc_i) for roc_i in toy]
toy_df = pd.concat(toy_listdf)

# start fn
y_true = np.array(y_true)
classes = np.unique(y_true)

if classes_to_plot is None:
    classes_to_plot = classes

indices_to_plot = np.array(np.where(np.isin(classes, classes_to_plot)))

models_true

toy = {"a", "b"}
toy.items()
models_true = "Model: "

# Test dict type to fix below
# https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance
# https://stackoverflow.com/questions/25231989/how-to-check-if-a-variable-is-a-dictionary-in-python

# do it for precision recall and other curves
# https://github.com/reiinakano/scikit-plot/blob/master/scikitplot/metrics.py

fig = go.Figure()
for model_label, probas_model in probas_dict.items():
    for i, probas_i in enumerate(probas_model.T):
        fpr, tpr, thresholds = metrics.roc_curve(
            y_true, probas_i, pos_label=classes[i]
        )
        roc_auc = metrics.auc(fpr, tpr)
        hover_txt = [
            models_true + model_label + ", Class: " + str(classes[i]) + "<br>" +
            "<b>Threshold: " + "{:.4f}".format(thr_i) + "</b><br><br>" +
            "True Positive Rate: " + "{:.2%}".format(tpr_i) + "<br>" +
            "False Positive Rate: " + "{:.2%}".format(fpr_i)
            for thr_i, fpr_i, tpr_i in zip(thresholds, fpr, tpr)
        ]
        fig.add_trace(
            go.Scatter(
                x=fpr,
                y=tpr,
                mode="lines",
                name=str(classes[i]) + ", " + model_label,
                legendgroup=str(classes[i]),
                hovertext=hover_txt,
                hoverinfo="text"
            )
        )
        fig.add_trace(
            go.Scatter(
                x=fpr,
                y=tpr,
                mode="lines",
                name=model_label + ", " + str(classes[i]),
                legendgroup=model_label,
                hovertext=hover_txt,
                hoverinfo="text",
                line={"dash": "dash"},
                visible="legendonly"
            )
        )

fig.update_xaxes(title_text="False Positive Rate", range=[-0.01, 1])
fig.update_yaxes(title_text="True Positive Rate", range=[0, 1.01])
fig.update_layout(
    xaxis={"showspikes": True},
    yaxis={"showspikes": True},
    margin={"l": 15, "t": 15, "b": 15, "r": 15},
    legend={"x": 1, "y": 0, "xanchor": "right", "yanchor": "bottom"}
)

import plotly.express as px
fig = px.line(
    toy_df,
    x="fpr",
    y="tpr",
    labels={"ds"},
    color="model",
    line_group="class",
    hover_name="thresholds"
)
fig.show()

fpr_dict = dict()
tpr_dict = dict()

indices_to_plot = np.in1d(classes, classes_to_plot)
for i, to_plot in enumerate(indices_to_plot):
    fpr_dict[i], tpr_dict[i], _ = roc_curve(
        y_true, probas[:, i], pos_label=classes[i]
    )
    if to_plot:
        roc_auc = auc(fpr_dict[i], tpr_dict[i])
        color = plt.cm.get_cmap(cmap)(float(i) / len(classes))
        ax.plot(
            fpr_dict[i],
            tpr_dict[i],
            lw=2,
            color=color,
            label='ROC curve of class {0} (area = {1:0.2f})'
            ''.format(classes[i], roc_auc)
        )

if plot_micro:
    binarized_y_true = label_binarize(y_true, classes=classes)
    if len(classes) == 2:
        binarized_y_true = np.hstack((1 - binarized_y_true, binarized_y_true))
    fpr, tpr, _ = roc_curve(binarized_y_true.ravel(), probas.ravel())
    roc_auc = auc(fpr, tpr)
    ax.plot(
        fpr,
        tpr,
        label='micro-average ROC curve '
        '(area = {0:0.2f})'.format(roc_auc),
        color='deeppink',
        linestyle=':',
        linewidth=4
    )

if plot_macro:
    # Compute macro-average ROC curve and ROC area
    # First aggregate all false positive rates
    all_fpr = np.unique(
        np.concatenate([fpr_dict[x] for x in range(len(classes))])
    )

    # Then interpolate all ROC curves at this points
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(len(classes)):
        mean_tpr += interp(all_fpr, fpr_dict[i], tpr_dict[i])

    # Finally average it and compute AUC
    mean_tpr /= len(classes)
    roc_auc = auc(all_fpr, mean_tpr)

    ax.plot(
        all_fpr,
        mean_tpr,
        label='macro-average ROC curve '
        '(area = {0:0.2f})'.format(roc_auc),
        color='navy',
        linestyle=':',
        linewidth=4
    )

ax.plot([0, 1], [0, 1], 'k--', lw=2)
ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.05])
ax.set_xlabel('False Positive Rate', fontsize=text_fontsize)
ax.set_ylabel('True Positive Rate', fontsize=text_fontsize)
ax.tick_params(labelsize=text_fontsize)
ax.legend(loc='lower right', fontsize=text_fontsize)
