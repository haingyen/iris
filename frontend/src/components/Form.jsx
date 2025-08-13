import { useState } from 'react';

const PostForm = () => {
  const [formData, setFormData] = useState({
    sepalLength: '',
    sepalWidth: '',
    petalLength: '',
    petalWidth: ''
  });
  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      setMessage(data.prediction);
    } catch (error) {
      setMessage('Error submitting form');
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Iris </h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Sepal Length - cm:</label>
          <input
            type="text"
            name="sepalLength"
            value={formData.sepalLength}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Sepal Width - cm:</label>
          <input
            type="text"
            name="sepalWidth"
            value={formData.sepalWidth}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Petal Length - cm:</label>
          <input
            type="text"
            name="petalLength"
            value={formData.petalLength}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Petal Width - cm:</label>
          <input
            type="text"
            name="petalWidth"
            value={formData.petalWidth}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Submit</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default PostForm;