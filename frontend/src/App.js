import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import TableBooking from "./pages/TableBooking";
import { Toaster } from "./components/ui/toaster";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<TableBooking />} />
        </Routes>
      </BrowserRouter>
      <Toaster />
    </div>
  );
}

export default App;