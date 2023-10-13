const Skeleton = () => {
  return (
    <>
      <main
        className="grid sm:grid-cols-2 md:grid-cols-1 gap-x-3 mt-5"
        id="domains"
      >
        <div className="px-5 md:px-5 lg:px-16 flex flex-wrap justify-center gap-3">
          {[...Array(6)].map((_, index) => (
            <div
              key={index}
              className="w-full lg:my-4 lg:px-4 max-w-sm p-6 bg-white border border-gray-200 rounded-md shadow animate-pulse"
            >
              <div className="h-6 bg-gray-300 rounded w-3/4 mb-4"></div>
              <div className="h-4 bg-gray-300 rounded w-1/2 mb-2"></div>
              <div className="h-4 bg-gray-300 rounded w-3/4 mb-2"></div>
              <div className="h-4 bg-gray-300 rounded w-2/4 mb-2"></div>
              <div className="h-4 bg-gray-300 rounded w-3/4 mb-2"></div>
              <div className="h-4 bg-gray-300 rounded w-1/4"></div>
            </div>
          ))}
        </div>
      </main>
    </>
  );
};

export default Skeleton;
