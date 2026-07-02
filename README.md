# QuenchLab — Interactive Heat Treatment Simulator

An interactive web-based heat treatment simulator that predicts alloy phase transformation and hardness based on cooling rate. The project combines metallurgical principles with Python and JavaScript to visualize Continuous Cooling Transformation (CCT) behavior in engineering alloys.



## Features

- Interactive cooling-rate simulator
- Live phase fraction visualization
- Hardness prediction for multiple alloys
- Dynamic hardness vs cooling-rate graph
- Python-based analytical model
- CSV export of hardness predictions
- Comparative visualization across alloy systems


## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js

### Backend
- Python
- Pandas
- Matplotlib
- NumPy




## Working Principle

The simulator approximates Continuous Cooling Transformation (CCT) behavior using a simplified computational model.

- Cooling rate determines the phase transformation.
- Phase fractions are estimated using Gaussian-based affinity functions.
- Final hardness is calculated as the weighted average of individual phase hardness values.

Although simplified, the model effectively demonstrates the relationship between cooling rate, microstructure, and hardness in engineering alloys.


## Screenshots

### Home Interface

![Home](images/home.png)

### Hardness Prediction

![Graph](images/graph.png)

### Phase Transformation


### Clone Repository

```bash
git clone https://github.com/Arundhathi2425/QuenchLab.git
cd QuenchLab
```

### Install Dependencies

```bash
pip install pandas matplotlib numpy
```

### Run Python Analysis

```bash

python quenchlab_analysis.py
```

The script generates:

- `hardness_vs_cooling_rate.png`
- `hardness_predictions.csv`

---

## Future Enhancements

- Integrate real TTT/CCT datasets
- Add tempering simulation
- Include Jominy End Quench comparison
- Predict tensile strength and toughness
- Export simulation reports
