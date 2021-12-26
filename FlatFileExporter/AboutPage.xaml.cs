using FlatFileExporter.Models;
using Newtonsoft.Json;
using RestSharp;
using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Controls;


namespace FlatFileExporter
{
    /// <summary>
    /// Interaction logic for AboutPage.xaml
    /// </summary>
    public partial class AboutPage : Page
    {
        public AboutPage()
        {
            InitializeComponent();
        }

        public string vrsn = "0.1.5";

        #region Support Links to repo

        private void btnSupportDocs(object sender, RoutedEventArgs e)
        {
            Process.Start("https://github.com/eddyizm/flatfileexporter");
            e.Handled = true;
        }

        private void btnIssues(object sender, RoutedEventArgs e)
        {
            Process.Start("https://github.com/eddyizm/flatfileexporter/issues");
            e.Handled = true;
        }

        private void btnCoffee(object sender, RoutedEventArgs e)
        {
            Process.Start("https://ko-fi.com/eddyizm");
            e.Handled = true;
        }

        #endregion

        private void test(object sender, RoutedEventArgs e)
        {
            Console.WriteLine("hello");
            checkversion();
            
        }

        private void Contribute_Expanded(object sender, RoutedEventArgs e)
        {
            CurrentIssues.IsExpanded = false;
        }

        private void checkversion()
        {
            string caption = "Checking Version...";
            try
            {
                // dev
                // var client = new RestClient("http://127.0.0.1:8000/api/v1/flat_file_version");
                var client = new RestClient("https://eddyizm.com/api/v1/flat_file_version");
                client.Timeout = -1;
                var request = new RestRequest(Method.GET);
                IRestResponse response = client.Execute(request);
                var result = JsonConvert.DeserializeObject<VersionCheck>(response.Content);

                var version1 = new Version(result.version);
                var version2 = new Version(vrsn);
                var versionResult = version1.CompareTo(version2);
                

                if (versionResult > 0)
                {
                    MessageBoxButton button = MessageBoxButton.YesNo;
                    MessageBoxResult mresult;
                    mresult = MessageBox.Show($"New Version Available: {result.version}\n" +
                    $"Last Updated: {String.Format("{0:d}", result.dateUpdated)}\n" +
                    $"Update", caption, button);
                    if (mresult == MessageBoxResult.Yes)
                    {
                        Process.Start(result.URL);
                    }

                }
                else
                {
                    MessageBox.Show($"Software Up to Date: {vrsn}\n");
                }
                
            }
            catch (Exception)
            {
                MessageBox.Show($"Error contacting Server. Please try again later.", caption);
            }


        }

    }
}


    