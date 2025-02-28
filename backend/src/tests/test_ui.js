import { render, screen, fireEvent } from "@testing-library/react";
import Summarizer from "../components/Summarizer";  // Ensure correct path

test("renders input box", () => {
  render(<Summarizer />);
  const inputElement = screen.getByPlaceholderText("Enter text to summarize...");
  expect(inputElement).toBeInTheDocument();
});

test("renders submit button", () => {
  render(<Summarizer />);
  const buttonElement = screen.getByText("Summarize");
  expect(buttonElement).toBeInTheDocument();
});

test("handles API call", async () => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      json: () => Promise.resolve({ summary: "This is a test summary." }),
    })
  );

  render(<Summarizer />);
  fireEvent.click(screen.getByText("Summarize"));
  expect(await screen.findByText("This is a test summary.")).toBeInTheDocument();
});
