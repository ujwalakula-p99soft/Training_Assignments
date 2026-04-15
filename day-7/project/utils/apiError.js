export const errorHandler = (err, _req, res, _next) => {
  const statusCode = err.statusCode || 500;
  const errorCode = err.code || "INTERNAL_SERVER_ERROR";

  const message =
    statusCode === 500
      ? "Server Error. Please try again later."
      : err.message || "Something went wrong";

  console.error(err);

  res.status(statusCode).json({
    success: false,
    error: {
      code: errorCode,
      message,
    },
  });
};