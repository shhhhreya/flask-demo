# K-Means Clustering Visualizer Project

## Problem Statement

**Objective:** Build an interactive K-Means Clustering visualizer for educational purposes.

The aim of this project is to create a web application that demonstrates the K-Means clustering algorithm in an interactive and visually engaging way. The visualizer will allow users to generate datasets, choose the number of clusters (`k`), and watch the algorithm's progress through each iteration. This app will also include controls to restart the algorithm, adjust the number of clusters, and visualize each step of the K-Means process.

### Project Goals
1. Allow users to generate and visualize different datasets.
2. Enable users to select the number of clusters (`k`).
3. Display each iteration of the K-Means algorithm, showing how centroids are updated and data points are assigned to clusters.
4. Provide UI elements like buttons and sliders to control the algorithm.

---

## Tech Stack

**Frontend:**
- **HTML/CSS**: For basic structure and styling.
- **JavaScript with Plotly.js**: For interactive data visualization and real-time updates.

**Backend:**
- **Flask (Python)**: To handle K-Means calculations and interact with the frontend.

**Other Tools:**
- **NumPy** (Python): For efficient mathematical operations in K-Means computations.
- **Plotly.js**: For client-side interactive and animated visualizations.

This stack leverages Flask for Python-based backend computations, enabling quick interactions with JavaScript and Plotly on the frontend.

---

## Project Features and Requirements

### 1. Dataset Generator
- **Generate a sample dataset** using clusters for visual distinction.
- **Dataset Shapes**: Allow users to select from pre-defined data shapes (e.g., circular clusters, blobs).

### 2. K-Means Clustering Steps
- **Display Initial Centroids**: Show initial centroids, either randomly or using k-means++ initialization.
- **Assignments and Updates**: In each iteration, display data points being assigned to the nearest centroid and centroids updating their positions.

### 3. User Controls
- **Slider for `k` Value**: Adjusts the number of clusters dynamically.
- **Step-by-Step Control**: Allows users to go through each iteration of K-Means.
- **Reset Button**: Resets the dataset and centroids to start over.

### 4. Visualization Features
- **Color-Coded Clusters**: Different colors represent each cluster.
- **Animated Centroid Movements**: Show centroid shifts and data point reassignments in real-time.

---

## Project Timeline

### Day 1-2: Backend Setup and Data Generation
- Set up Flask to serve the web app and handle data generation.
- Create a Python function to generate random datasets and compute initial centroids.
- Implement basic K-Means functions for assigning clusters and updating centroids.
- Test clustering functions independently to ensure correctness.

### Day 3: Frontend Structure and Basic Visualization
- Set up basic HTML structure and integrate Plotly.js.
- Create a static graph to display initial data points.
- Set up Flask endpoints to pass dataset and centroid data to the frontend.

### Day 4: Real-Time Visualizations
- Implement JavaScript functions to request updated centroid and cluster data from Flask.
- Use Plotly.js to update the visualization with each iteration’s data points and centroid positions.
- Test the visualization to ensure smooth updates and transitions.

### Day 5: User Controls and Interactivity
- Add sliders for selecting the number of clusters and buttons for controlling algorithm steps.
- Connect the controls to the backend, allowing users to reset, iterate, and change `k`.
- Implement dynamic dataset generation based on user input for clusters.

### Day 6: Refinement and Finishing Touches
- Refine user interface elements (labels, instructions).
- Optimize for responsiveness and user experience.
- Add explanatory text to guide users through the app and explain what each part of the visualizer does.

### Day 7: Testing and Documentation
- Run final tests to ensure smooth app performance.
- Write documentation on the code, usage, and insights on the K-Means algorithm.
- Deploy (optional) to a platform like Heroku for easy sharing.
