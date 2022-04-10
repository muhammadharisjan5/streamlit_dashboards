from sklearn.datasets import load_iris
iris= load_iris()
# Store features matrix in X
X= iris.data
#Store target vector in 
y= iris.target


# Run a PCA
@st.cache
def run_pca():
    # Run PCA
    pca = PCA(2)
    X = df.iloc[:, :4]
    X_pca = pca.fit(X).transform(X)
    df_pca = pd.DataFrame(pca.transform(X))
    df_pca.columns = ['PC1', 'PC2']
    df_pca = pd.concat([df_pca, df['variety']], axis=1)
    
    return pca, df_pca

pca, df_pca = run_pca()
# Create the PCA chart
pca_fig = px.scatter(
    df_pca, 
    x='PC1', 
    y='PC2', 
    color='variety', 
    hover_name='variety', 
    width=500, 
    height=350)

# Retrieve user input
datapoint = np.array([[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]])
# Map the 4-D user input to 2-D using the PCA
datapoint_pca = pca.transform(datapoint)
# Add the user input to the PCA chart
pca_fig.add_trace(go.Scatter(
        x=[datapoint_pca[0, 0]], 
        y=[datapoint_pca[0,1]], 
        mode='markers', 
        marker={'color': 'black', 'size':10}, name='Your Datapoint'))

with col2:
    st.markdown('### Principle Component Analysis')
    pca_fig

